from django.db import transaction
from ..models import *
from .convert_date import convert_date_format


def create_or_get_province(province_name):
    province_obj, __ = Province.objects.get_or_create(
        province_name=province_name)
    return province_obj


def create_or_get_district(district_name, province_obj):
    district_obj, __ = District.objects.get_or_create(
        district_name=district_name, province=province_obj)
    return district_obj


def create_or_get_municipality(municipality_name, district_obj):
    municipality_obj, __ = Municipality.objects.get_or_create(
        municipality_name=municipality_name, district=district_obj)
    return municipality_obj


def create_or_get_donor(donor_name):
    donor_obj, __ = Donor.objects.get_or_create(donor_name=donor_name)
    return donor_obj


def create_or_get_counterpart_ministry(counterpart_ministry_name):
    counterpart_ministry_obj, __ = CounterpartMinistry.objects.get_or_create(
        counterpart_ministry_name=counterpart_ministry_name)
    return counterpart_ministry_obj


def create_or_get_many_fields(fields_, Model, model_field):
    """
    It either creates a new instance of a Model or get already existing object.
    Use when there is many-to-many relation with Projects model

    Args:
        fields_ (str): value inside somefield in row 
        Model (type(django.models)): Django model that is in many-to-many relation with Project model
        model_field (str): field of Model

    Returns:
        list(model objects): A list of all obj that are either created or fetched
    """
    objs = []

    for value in fields_.split(","):
        obj, __ = Model.objects.get_or_create(**{model_field: value.strip()})
        objs.append(obj)

    return objs


@transaction.atomic
def create_project_instance(row) -> None:
    """
    Creates a Project instance based on the data in the given row.

    Args:
        row: A dictionary-like object containing the data for the project. Must have the following keys:
            - "Province": A string representing the name of the province where the project is located.
            - "District": A string representing the name of the district where the project is located.
            - "Municipality": A string representing the name of the municipality where the project is located.
            - "Donor": A string representing the name of the donor funding the project.
            - "Counterpart Ministry": A string representing the name of the ministry in the project's counterpart government.
            - "Agreement Date": A string representing the date on which the agreement for the project was made, in the format "dd/mm/yyyy".
            - "Commitments": A number representing the total amount of money committed to the project.
            - "Disbursement": A number representing the total amount of money disbursed for the project.
            - "Executing Agency": A string representing the name of the executing agency or agencies for the project, separated by commas if there are multiple agencies.
            - "Implementing Partner": A string representing the name of the implementing partner or partners for the project, separated by commas if there are multiple partners.
            - "Type of Assistance": A string representing the type or types of assistance provided for the project, separated by commas if there are multiple types.
            - "Sector": A string representing the sector or sectors to which the project belongs, separated by commas if there are multiple sectors.

    Returns:
        None
    """

    try:
        # Get object for following models, if exists, else create it
        province_obj = create_or_get_province(row["Province"])
        district_obj = create_or_get_district(row["District"], province_obj)
        municipality_obj = create_or_get_municipality(
            row["Municipality"], district_obj)

        donor_obj = create_or_get_donor(row["Donor"])
        counterpart_ministry_obj = create_or_get_counterpart_ministry(
            row["Counterpart Ministry"])

        agreement_date = convert_date_format(
            # Agreement Date can be empty which case None is used
            row["Agreement Date"]) if row["Agreement Date"] != "" else None
        agreement_obj, __ = Agreement.objects.get_or_create(
            agreement_date=agreement_date, defaults={"agreement_date": agreement_date})

        commitment_disbursement_obj, _ = CommitmentDisbursement.objects.get_or_create(
            commitment=row["Commitments"],
            # Disbursement can be empty string in which case set None
            disbursement=row["Disbursement"] if row["Disbursement"] != "" else None
        )

        executing_agencies_obj = create_or_get_many_fields(
            row["Executing Agency"], ExecutingAgency, "executing_agency_name")

        implementing_partner_obj = create_or_get_many_fields(
            row["Implementing Partner"], ImplementingPartner, "implementing_partner_name"
        )

        type_of_assitance_obj = create_or_get_many_fields(
            row["Type of Assistance"], TypeOfAssistance, "type_of_assistance"
        )

        sector_obj = create_or_get_many_fields(
            row["Sector"], Sector, "sector_name")

        # create project instance
        project_obj, __ = Project.objects.get_or_create(
            project_title=row["Project Title"],
            project_status=row["Project Status"],
            budget_type=row["Budget Type"],
            humanitarian=row["Humanitarian"],
            municipality=municipality_obj,
            agreement=agreement_obj,
            commitment_disbursement=commitment_disbursement_obj,
            counterpart_ministry=counterpart_ministry_obj,
            donor=donor_obj,
        )

        # single project might contain many type of assitance
        project_obj.type_of_assistance.set(type_of_assitance_obj)
        # single project might contain many executing agency
        project_obj.executing_agency.set(executing_agencies_obj)
        # single project might contain many implementing partner
        project_obj.implementing_partner.set(implementing_partner_obj)
        # single project might contain many sectors
        project_obj.project_sector.set(sector_obj)

    except Exception as e:
        raise e
