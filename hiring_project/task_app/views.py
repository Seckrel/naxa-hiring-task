from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Project)
from django.db.models import Prefetch
from .serializer import ProjectSerializer


class UploadSheet(APIView):
    def post(self, request):
        pass


class ListProjectAndFilter(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        self.queryset = self.queryset.prefetch_related("sectors", "partners", "").filter(
            commitment_disbursement_id__commitment__gte=5000)

    def get(self, request):
        response_data = {}

        try:
            queryset = Project.objects.filter(
                commitment_disbursement__commitment__exact=5000
            )

            serializer = self.serializer_class(queryset, many=True)
            response_data["data"] = serializer.data
            response_data["success"] = True
        except Exception as e:
            response_data["success"] = False
            response_data["error"] = str(e)

        return Response(status=200, data=response_data)


class SummaryOfProject(APIView):
    def get(self, request):
        pass


class CountProjectsAndBudgets(APIView):
    def get(self, request):
        pass
