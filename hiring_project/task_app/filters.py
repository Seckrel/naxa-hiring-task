from .models import Project
import django_filters


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'project_title': ['icontains'],
            'project_status': ['exact'],
            'budget_type': ['exact'],
            'humanitarian': ['exact'],
            'municipality__municipality_name': ['icontains'],
            'agreement__agreement_date': ['gte', 'lte'],
            'commitment_disbursement__commitment': ['gte', 'lte', 'exact'],
            'commitment_disbursement__disbursement': ['gte', 'lte', 'exact'],
            'donor__donor_name': ['icontains'],
            'type_of_assistance': ['exact',],
            'executing_agency': ['icontains'],
            'implementing_partner': ['icontains'],
            'project_sector__sector_name': ['exact', "icontains"]
        }
