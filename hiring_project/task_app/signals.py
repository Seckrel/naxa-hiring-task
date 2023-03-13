from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import *
from django.core.exceptions import ValidationError

from .utils.validate_project import *


@receiver(pre_save, sender=Province)
def validate_province(sender, instance, **kwargs):
    province_name = instance.province_name

    if not check_is_str(province_name) or check_is_null(province_name):
        raise ValidationError("Province name cannot be empty or numeric")


@receiver(pre_save, sender=District)
def validate_district(sender, instance, **kwargs):
    district_name = instance.district_name

    if not check_is_str(district_name) or check_is_null(district_name):
        raise ValidationError("Distric name cannot be empty or numeric")


@receiver(pre_save, sender=Municipality)
def validate_municiaplity(sender, instance, **kwargs):
    municipality_name = instance.municipality_name

    if not check_is_str(municipality_name) or check_is_null(municipality_name):
        raise ValidationError("Municipality name cannot be empty or numeric")


@receiver(pre_save, sender=CommitmentDisbursement)
def validate_commitment_disbursement(sender, instance, **kwargs):
    commitment = instance.commitment
    disbursement = instance.disbursement

    if not check_is_int(commitment) or check_is_null(commitment):
        raise ValidationError(
            "Commitment cannot be empty and has to be whole number")

    if check_is_null(disbursement):
        return

    if not check_is_float(disbursement):
        raise ValidationError(
            "Disbursement has to be a number (can also be decimal point number)")


@receiver(pre_save, sender=Donor)
def validate_donor(sender, instance, **kwargs):
    donor_name = instance.donor_name

    if not check_is_str(donor_name) or check_is_null(donor_name):
        raise ValidationError("Donor name cannot be empty or numeric")


@receiver(pre_save, sender=TypeOfAssistance)
def validate_type_of_assitance(sender, instance, **kwargs):
    type_of_assistance = instance.type_of_assistance
    range_of_possible_values = ["ta", "grant", "loan"]

    if check_is_null(type_of_assistance) or not check_is_str(type_of_assistance) or \
            not check_in_range(type_of_assistance, range_of_possible_values):

        raise ValidationError(
            "Type of assitance can only be TA, Grant, or Loan")


@receiver(pre_save, sender=ExecutingAgency)
def validate_executing_agency(sender, instance, **kwargs):
    executing_agency_name = instance.executing_agency_name

    if not check_is_str(executing_agency_name) or check_is_null(executing_agency_name):
        raise ValidationError("Executing Agency cannot be empty or numeric")


@receiver(pre_save, sender=ImplementingPartner)
def validate_implementing_partnet(sender, instance, **kwargs):
    implementing_partner_name = instance.implementing_partner_name

    if not check_is_str(implementing_partner_name) or check_is_null(implementing_partner_name):
        raise ValidationError(
            "Implementing Partner cannot be empty or numeric")


@receiver(pre_save, sender=Sector)
def validate_sector(sender, instance, **kwargs):
    sector_name = instance.sector_name

    if not check_is_str(sector_name) or check_is_null(sector_name):
        raise ValidationError("Sector of Project cannot be empty or numeric")


@receiver(pre_save, sender=Agreement)
def validate_agreement(sender, instance, **kwargs):
    agreement = instance.agreement_date

    if check_is_null(agreement):
        return

    if not check_is_date(agreement):
        raise ValidationError("Agreement fields must be a date")


@receiver(pre_save, sender=CounterpartMinistry)
def validate_counterpart_ministry(sender, instance, **kwargs):
    counterpart_ministry_name = instance.counterpart_ministry_name

    if not check_is_str(counterpart_ministry_name) or check_is_null(counterpart_ministry_name):
        raise ValidationError(
            "Name of Counterpart Ministry cannot be empty or numeric")


@receiver(pre_save, sender=Project)
def validate_project(sender, instance, **kwargs):
    project_title = instance.project_title
    project_status = instance.project_status
    budget_type = instance.budget_type
    humanitarian = instance.humanitarian

    budget_type_range = ["on budget", "off budget"]
    humanitarian_range = ["yes", "no"]

    if not check_is_str(project_title) or check_is_null(project_title):
        raise ValidationError("Project title cannot be empty or numeric")

    if not check_is_str(project_status) or check_is_null(project_status):
        raise ValidationError("Project status cannot be empty or numeric")

    if not check_is_str(budget_type) or check_is_null(budget_type) or not check_in_range(budget_type, budget_type_range):
        raise ValidationError(
            "Budget type can only be either on budget or off budget")

    if not check_is_str(humanitarian) or check_is_null(humanitarian) or not check_in_range(humanitarian, humanitarian_range):
        raise ValidationError("Humanitarian type can only be either yes or no")
