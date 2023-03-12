from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Project
from .serializer import ProjectSerializer


class ListProjectAndFilterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse('task_app:list_projects')

    def test_list_project_and_filter_district_name(self):
        list_of_district_name = [
            "Surkhet (Surkhet)", "Rukum (Western part)", "Mugu (Gamgadhi)"]

        for district_name in list_of_district_name:
            response = self.client.get(
                self.url, {'municipality__district__district_name__icontains': district_name})

            queryset = Project.objects.filter(
                municipality__district__district_name__icontains=district_name)

            serializer = ProjectSerializer(queryset, many=True)

            self.assertEqual(response.data, serializer.data)

    def test_list_project_and_filter_commitment_gte(self):
        list_of_values = [50000, 60000, 100000]

        for values in list_of_values:
            response = self.client.get(
                self.url, {'commitment_disbursement__commitment__gte': values}
            )

            queryset = Project.objects.filter(
                commitment_disbursement__commitment__gte=values
            )

            serializer = ProjectSerializer(queryset, many=True)

            self.assertEqual(response.data, serializer.data)

        for values in list_of_values:
            response = self.client.get(
                self.url, {'commitment_disbursement__commitment__lte': values}
            )

            queryset = Project.objects.filter(
                commitment_disbursement__commitment__lte=values
            )

            serializer = ProjectSerializer(queryset, many=True)

            self.assertEqual(response.data, serializer.data)

    def test_list_project_and_filter_toa_icontains(self):
        list_toa = ['ta', 'grant', 'loan']

        for toa in list_toa:
            response = self.client.get(
                self.url, {
                    'type_of_assistance__type_of_assistance__icontains': toa}
            )

            queryset = Project.objects.filter(
                type_of_assistance__type_of_assistance__icontains=toa
            )

            serializer = ProjectSerializer(queryset, many=True)

            self.assertEqual(response.data, serializer.data)


class CountProjectsAndBudgets(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.url = reverse("task_app:summaraize_project")

    def test_summary_project_sector_name(self):
        list_sector_name = ["agriculture", "health", "Housing", "Supply"]

        for sector_name in list_sector_name:

            response = self.client.get(
                self.url, {
                    'project_sector__sector_name__icontains': sector_name}
            )

            queryset = Project.objects.filter(
                project_sector__sector_name__icontains=sector_name
            )

            serializer = ProjectSerializer(queryset, many=True)

            self.assertEqual(response.data, serializer.data)
