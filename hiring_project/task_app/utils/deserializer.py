from ..models import *
from .convert_date import convert_date_format


def multiple_fields_object_creator(field, Model, model_field):
    field_list = field.split(",")

    field_obj = []

    for field_ in field_list:
        obj, __ = Model.objects.get_or_create(**{model_field: field_})

        field_obj.append(obj)

    return field_obj


def create_project_instance(row):
    province_obj, __ = Province.objects.get_or_create(
        province_name=row["Province"])

    district_obj, __ = District.objects.get_or_create(
        district_name=row["District"], province=province_obj)

    municipality_obj, __ = Municipality.objects.get_or_create(
        municipality_name=row["Municipality"], district=district_obj)

    donor_obj, __ = Donor.objects.get_or_create(
        donor_name=row["Donor"])

    executing_agencies_obj = multiple_fields_object_creator(
        row["Executing Agency"], ExecutingAgency, "executing_agency_name")

    implementing_partner_obj = multiple_fields_object_creator(
        row["Implementing Partner"], ImplementingPartner, "implementing_partner_name")

    counterpart_ministry_obj, __ = CounterpartMinistry.objects.get_or_create(
        counterpart_ministry_name=row["Counterpart Ministry"]
    )

    type_of_assitance_obj = multiple_fields_object_creator(
        row["Type of Assistance"], TypeOfAssistance, "type_of_assistance"
    )

    sector_obj = multiple_fields_object_creator(
        row["Sector"], Sector, "sector_name"
    )

    agreement_obj, __ = Agreement.objects.get_or_create(
        agreement_date=convert_date_format(row["Agreement Date"])) if row["Agreement Date"] != "" else (None, None)

    commitment_disbursement_obj, _ = CommitmentDisbursement.objects.get_or_create(
        commitment=row["Commitments"],
        disbursement=row["Disbursement"] if row["Disbursement"] != "" else None
    )

    project_obj, project_created = Project.objects.get_or_create(
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

    for ta in type_of_assitance_obj:
        project_obj.type_of_assistance.add(ta)

    for ea in executing_agencies_obj:
        project_obj.executing_agency.add(ea)

    for ip in implementing_partner_obj:
        project_obj.implementing_partner.add(ip)

    for s in sector_obj:
        project_obj.project_sector.add(s)
