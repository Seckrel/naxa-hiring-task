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
    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    # def get(self, request):
    #     response_data = {}

    #     try:
    #         queryset = Project.objects.filter(
    #             commitment_disbursement__commitment__exact=5000
    #         )

    #         serializer = self.serializer_class(queryset, many=True)
    #         response_data["data"] = serializer.data
    #         response_data["success"] = True
    #     except Exception as e:
    #         response_data["success"] = False
    #         response_data["error"] = str(e)

    #     return Response(status=200, data=response_data)


class SummaryOfProject(APIView):
    def get(self, request):
        pass


class CountProjectsAndBudgets(APIView):
    def get(self, request):
        pass
