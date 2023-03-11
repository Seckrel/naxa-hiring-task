from django.urls import path
from .views import UploadSheet, ListProjectAndFilter, SummaryOfProject, CountProjectsAndBudgets

urlpatterns = [
    path("upload-csv/", UploadSheet.as_view(), name="csv_to_db"),
    path("projects/", ListProjectAndFilter.as_view(), name="list_projects"),
    path("summary/", SummaryOfProject.as_view(), name="summaraize_project"),
    path("count-projects-budget/", CountProjectsAndBudgets.as_view(),
         name="count_projects_budget")

]
