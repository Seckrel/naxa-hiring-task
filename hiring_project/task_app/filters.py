from .models import Project
import django_filters


class ProjectFilter(django_filters.FilterSet):
    '''
    A FilterSet class to filter the Project model based on various attributes.

    Attributes:
        model: The Project model to which the filter applies.
        fields: A dictionary mapping filter fields to their lookups.

    Filter fields:
        project_title: Filter by the title of the project (case-insensitive).
        project_status: Filter by the status of the project (exact match).
        budget_type: Filter by the budget type of the project (exact match).
        humanitarian: Filter by whether the project is humanitarian or not (exact match).
        municipality__municipality_name: Filter by the name of the municipality in which the project is located (exact match).
        municipality__district__district_name: Filter by the name of the district in which the project is located (exact match).
        agreement__agreement_date: Filter by the date of the agreement (greater than or equal to, less than or equal to).
        commitment_disbursement__commitment: Filter by the commitment amount (greater than or equal to, less than or equal to, exact match).
        commitment_disbursement__disbursement: Filter by the disbursement amount (greater than or equal to, less than or equal to, exact match).
        donor__donor_name: Filter by the name of the donor (case-insensitive).
        type_of_assistance: Filter by the type of assistance provided (exact match).
        executing_agency: Filter by the name of the executing agency (case-insensitive).
        implementing_partner: Filter by the name of the implementing partner (case-insensitive).
        project_sector__sector_name: Filter by the name of the project sector (exact match or case-insensitive match).
    '''

    class Meta:
        model = Project
        fields = {
            'project_title': ['icontains'],
            'project_status': ['icontains'],
            'budget_type': ['icontains'],
            'humanitarian': ['icontains'],
            'municipality__municipality_name': ['icontains'],
            'municipality__district__district_name': ['icontains'],
            'agreement__agreement_date': ['gte', 'lte'],
            'commitment_disbursement__commitment': ['gte', 'lte', 'icontains'],
            'commitment_disbursement__disbursement': ['gte', 'lte', 'icontains'],
            'donor__donor_name': ['icontains'],
            'type_of_assistance': ['icontains',],
            'executing_agency': ['icontains'],
            'implementing_partner': ['icontains'],
            'project_sector__sector_name': ['icontains']
        }
