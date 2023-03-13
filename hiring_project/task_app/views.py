from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Sum, Count, F
from .models import Project

from .serializer import ProjectSerializer
from .filters import ProjectFilter
from .utils.deserializer import create_project_instance

from django.core.exceptions import ValidationError

import csv


class UploadSheet(APIView):
    """
    API View for uploading a CSV file of projects data and creating new Project instances.

    Attributes:
        parser_classes (tuple): A tuple of parser classes to handle the uploaded file.
        model (class): The model class for creating new Project instances.

    Methods:
        post(request): Handles the HTTP POST request for uploading the CSV file and creating new Project instances.
            Args:
                request (HttpRequest): The HTTP request object containing the uploaded file.

            Returns:
                Response: A Response object with a message indicating whether the upload was successful.
    """

    parser_classes = (MultiPartParser, FormParser)
    model = Project

    def post(self, request):
        file_obj = request.data['fileName']
        decoded_file = file_obj.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)

        try:
            for row in reader:
                create_project_instance(row)

        except ValidationError as e:
            return Response({"message": str(e)})

        except Exception as e:
            print(e)
            return Response({"message": "error in uploading csv"})

        return Response({"message": "upload completed"})


class ListProjectAndFilter(ListAPIView):
    """
    View for listing Project instances and filtering the list by various fields.

    E.g. Query: /api/v1/projects/?project_sector__sector_name__icontains=Health

    Attributes:
        serializer_class (class): The serializer class for serializing Project instances.
        filter_backends (list): A list of backend classes for filtering the queryset.
        filterset_class (class): The filterset class for filtering the queryset.

    Methods:
        get_queryset(): Returns the queryset of Project instances to be displayed.
            Returns:
                QuerySet: The queryset of Project instances to be displayed.
    """

    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        """
        Returns the queryset of Project instances to be displayed, filtered by the specified filters.

        Returns:
            QuerySet: The queryset of Project instances to be displayed.
        """

        queryset = Project.objects.all()
        return queryset


class SummaryOfProject(ListAPIView):
    """
    API View for generating a summary of Project instances, including the total number of projects, the total budget, 
    and a summary of projects by sector.

    E.g. Query: /api/v1/summary/?project_sector__sector_name__icontains=agriculture

    Attributes:
        filter_backends (list): A list of backend classes for filtering the queryset.
        filterset_class (class): The filterset class for filtering the queryset.

    Methods:
        get_queryset(): Returns the queryset of Project instances to be displayed.
            Returns:
                QuerySet: The queryset of Project instances to be displayed.

        list(request): Generates the summary of Project instances and returns a Response object.
            Args:
                request (HttpRequest): The HTTP request object for the view.

            Returns:
                Response: A Response object with a summary of Project instances.
    """

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        """
        Returns the queryset of Project instances to be displayed, filtered by the specified filters.

        Returns:
            QuerySet: The queryset of Project instances to be displayed.
        """

        queryset = Project.objects.all()
        return queryset

    def list(self, request):
        """
        Generates a summary of Project instances and returns a Response object.

        Args:
            request (HttpRequest): The HTTP request object for the view.

        Returns:
            Response: A Response object with a summary of Project instances.
        """

        queryset = self.filter_queryset(self.get_queryset())

        project_count = queryset.count()

        total_commitment = queryset.aggregate(Sum("commitment_disbursement__commitment"))[
            'commitment_disbursement__commitment__sum']

        total_disbursement = queryset.aggregate(Sum("commitment_disbursement__disbursement"))[
            'commitment_disbursement__disbursement__sum'
        ]

        budget = 0.0

        try:
            if total_disbursement is None:
                budget = total_commitment

            elif total_commitment is None:
                budget = total_disbursement

            else:
                budget = total_commitment - total_disbursement

        except TypeError as e:
            print(str(e))
            budget = 0

        sector_summary = queryset \
            .annotate(
                name=F("project_sector__sector_name"),
                id=F("project_sector__sector_id"),
                budget=Sum("commitment_disbursement__commitment") -
                Sum("commitment_disbursement__disbursement")
            ) \
            .values("id", "name", "budget",) \
            .annotate(
                project_count=Count('id')
            )

        serializer = {
            'project_count': project_count,
            'total_budget': budget,
            'sector': sector_summary
        }

        return Response(serializer)


class CountProjectsAndBudgets(ListAPIView):
    '''
    API View that returns a summary of the project count and budget for each municipality in the atabase.
    Summary report can be filtered based on municiaplity name and District name

    E.g. Query: /api/v1/count-projects-budget/?municipality__district__district_name__icontains=Surkhet (Surkhet)

    Attributes:
        filter_backends (list): A list of backend classes for filtering the queryset.
        filterset_class (class): The filterset class for filtering the queryset.
        filterset_fields (list): A list of fields that can be used to filter the project database

    Methods:
        get_queryset(): Returns the queryset of Project instances to be displayed.
            Returns:
                QuerySet: The queryset of Project instances to be displayed.

        list(request): It firstly filters the questset based on filter parameters. 
        It then annotates each project with the municipality name, ID, and budget of project 
        for grouped by municiaplity.
            Args:
                request (HttpRequest): The HTTP request object for the view.

            Returns:
                Response: A Response object with a summary of Project instances.

    '''
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    filterset_fields = ['municipality__municipality_name',
                        'municipality__district__district_name']

    def get_queryset(self):
        """
        Returns the queryset of Project instances to be displayed, filtered by the specified filters.

        Returns:
            QuerySet: The queryset of Project instances to be displayed.
        """

        queryset = Project.objects.all()
        return queryset

    def list(self, request):
        """
        Generates the summary report json of each project grouped by municiaplity name, and also counts
        project per municiaplity and their total budget

        Args:
            request (HttpRequest): The HTTP request object for the view.

        Returns:
            Response: A Response object with a summary of Project instances.
        """

        queryset = self.filter_queryset(self.get_queryset())

        municipality_summary = queryset \
            .annotate(
                name=F("municipality__municipality_name"),
                id=F("municipality__municipality_id"),
                budget=Sum("commitment_disbursement__commitment") -
                Sum("commitment_disbursement__disbursement")
            ) \
            .values("id", "name", "budget") \
            .annotate(
                count=Count('id')
            )

        return Response({"data": municipality_summary})
