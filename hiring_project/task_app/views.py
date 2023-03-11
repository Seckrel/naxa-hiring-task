from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, CommitmentDisbursement
from django.core import serializers


class UploadSheet(APIView):
    def post(self, request):
        pass


class ListProjectAndFilter(APIView):
    def get(self, request):
        fields = ['project_id', 'project_title', 'project_status', 'budget_type', 'humanitarian',
                  'municipality_id', 'projecttypeofassistance', 'projectexecutingagency',
                  'projectimplementingpartner', 'projectsector', 'agreement',
                  'agreement__donor_id', 'agreement__executing_agency_id',
                  'agreement__sector_id']

        projects = CommitmentDisbursement.objects.filter(
            commitment__gte=5000)

        serialized_data = serializers.serialize(
            'json', projects.values(*fields))
        print(serialized_data)
        return Response(status=200, data={"data", serialized_data})


class SummaryOfProject(APIView):
    def get(self, request):
        pass


class CountProjectsAndBudgets(APIView):
    def get(self, request):
        pass
