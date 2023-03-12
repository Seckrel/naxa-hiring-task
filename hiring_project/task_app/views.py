from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializer import ProjectSerializer
from .filters import ProjectFilter
import csv
from .utils.deserializer import create_project_instance
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count, F


class UploadSheet(APIView):
    parser_classes = (MultiPartParser, FormParser)
    model = Project

    def post(self, request):
        file_obj = request.data['fileName']
        decoded_file = file_obj.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)
        try:
            for row in reader:
                create_project_instance(row)
        except Exception as e:
            print(str(e))
            return Response({"message": "error in uploading csv"})

        return Response({"message": "upload completed"})


class ListProjectAndFilter(ListAPIView):
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


class SummaryOfProject(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        project_count = queryset.count()

        total_commitment = queryset.aggregate(Sum("commitment_disbursement__commitment"))[
            'commitment_disbursement__commitment__sum']

        total_disbursement = queryset.aggregate(Sum("commitment_disbursement__disbursement"))[
            'commitment_disbursement__disbursement__sum'
        ]

        budget = total_commitment - total_disbursement

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


class CountProjectsAndBudgets(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    filterset_fields = ['municipality__municipality_name',
                        'municipality__district__district_name']

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        print("-------------here")

        return Response({"data": queryset})
        pass
