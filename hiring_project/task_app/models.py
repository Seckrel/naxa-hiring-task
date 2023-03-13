from django.db import models
from django.core.validators import MinValueValidator


"""
Models:
- Province: a geographical province.
- District: a geographical district within a province.
- Municipality: a geographical municipality within a district.
- Donor: an organization that provides financial or material support for a project.
- ExecutingAgency: an organization responsible for executing a project.
- ImplementingPartner: an organization that partners with the executing agency to implement a project.
- CounterpartMinistry: a ministry or government agency that is a counterpart to the project.
- Sector: a sector or theme of the project.
- TypeOfAssistance: a type of financial assistance for the project.
- Agreement: an agreement associated with a project.
- CommitmentDisbursement: the commitment and disbursement associated with a project.
- Project: a project managed by the application.

Schema:
Schema 

Province
- ProvinceID (Primary Key)
- ProvinceName

District
- DistrictID (Primary Key)
- DistrictName
- ProvinceID (Foreign Key referencing Province table)

Municipality
- MunicipalityID (Primary Key)
- MunicipalityName
- DistrictID (Foreign Key referencing District table)

Donor
- DonorID (Primary Key)
- DonorName

ExecutingAgency
- ExecutingAgencyID (Primary Key)
- ExecutingAgencyName

ImplementingPartner
- ImplementingPartnerID (Primary Key)
- ImplementingPartnerName

CounterpartMinistry
- CounterpartMinistryID (Primary Key)
- CounterpartMinistryName

Sector
- SectorID (Primary Key)
- SectorName

Project
- ProjectID (Primary Key)
- ProjectTitle
- ProjectStatus
- TypesOfAssistance
- BudgetType
- Humanitarian
- MunicipalityID (Foreign Key referencing Municipality table)

ProjectExecutingAgency
- ProjectID (Foreign Key referencing Project table)
- ExecutingAgencyID (Foreign Key referencing ExecutingAgency table)
- PrimaryKey (ProjectID, ExecutingAgencyID)

ProjectImplementingPartner
- ProjectID (Foreign Key referencing Project table)
- ImplementingPartnerID (Foreign Key referencing ImplementingPartner table)
- PrimaryKey (ProjectID, ImplementingPartnerID)

ProjectCounterpartMinistry
- ProjectID (Foreign Key referencing Project table)
- CounterpartMinistryID (Foreign Key referencing CounterpartMinistry table)
- PrimaryKey (ProjectID, CounterpartMinistryID)

ProjectSector
- ProjectID (Foreign Key referencing Project table)
- SectorID (Foreign Key referencing Sector table)
- PrimaryKey (ProjectID, SectorID)

Agreement
- AgreementID (Primary Key)
- AgreementDate
- ProjectID (Foreign Key referencing Project table)
- DonorID (Foreign Key referencing Donor table)
- ExecutingAgencyID (Foreign Key referencing ExecutingAgency table)
- SectorID (Foreign Key referencing Sector table)

CommitmentDisbursement
- CommitmentDisbursementID (Primary Key)
- Commitment
- Disbursement
- AgreementID (Foreign Key referencing Agreement table)
The
    """


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.province_name


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="province")

    def __str__(self):
        return self.district_name


class Municipality(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    municipality_name = models.CharField(max_length=255, unique=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipality_name


class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    donor_name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.donor_name


class ExecutingAgency(models.Model):
    executing_agency_id = models.AutoField(primary_key=True)
    executing_agency_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.executing_agency_name


class ImplementingPartner(models.Model):
    implementing_partner_id = models.AutoField(primary_key=True)
    implementing_partner_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.implementing_partner_name


class CounterpartMinistry(models.Model):
    counterpart_ministry_id = models.AutoField(primary_key=True)
    counterpart_ministry_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.counterpart_ministry_name


class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.sector_name


class TypeOfAssistance(models.Model):
    TYPE_OF_ASSISTANCE_CHOICES = [
        ("TA", "TA"),
        ("Grant", "Grant"),
        ("Loan", "Loan"),
    ]

    type_of_assistance_id = models.AutoField(primary_key=True)
    type_of_assistance = models.CharField(
        max_length=6, choices=TYPE_OF_ASSISTANCE_CHOICES, unique=True)

    def __str__(self):
        return self.type_of_assistance


class Agreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    agreement_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.agreement_date}"


class CommitmentDisbursement(models.Model):
    commitment_disbursement_id = models.AutoField(primary_key=True)
    commitment = models.IntegerField(validators=[MinValueValidator(0)])
    disbursement = models.FloatField(
        validators=[MinValueValidator(0.0)], null=True)

    def __str__(self):
        return f"{self.commitment} | {self.disbursement}"


class Project(models.Model):
    BUDGET_TYPE_CHOICES = [
        ('Off Budget', "Off Budget"),
        ('On Budget', "On Budget")
    ]
    HUMANITARIAN_CHOICES = [
        ("No", "No"),
        ("Yes", "Yes")
    ]

    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=255)
    project_status = models.CharField(max_length=255)

    budget_type = models.CharField(max_length=25, choices=BUDGET_TYPE_CHOICES)
    humanitarian = models.CharField(max_length=3, choices=HUMANITARIAN_CHOICES)

    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, related_name="municipality")
    agreement = models.ForeignKey(
        Agreement, on_delete=models.CASCADE, related_name="agreement", null=True)
    commitment_disbursement = models.ForeignKey(
        CommitmentDisbursement, on_delete=models.CASCADE, related_name="commitment_disbursement")
    counterpart_ministry = models.ForeignKey(
        CounterpartMinistry, on_delete=models.CASCADE, related_name="counterpart_ministry",)

    donor = models.ForeignKey(
        Donor, on_delete=models.CASCADE, related_name="donor")

    type_of_assistance = models.ManyToManyField(
        TypeOfAssistance)

    executing_agency = models.ManyToManyField(
        ExecutingAgency)

    implementing_partner = models.ManyToManyField(
        ImplementingPartner)

    project_sector = models.ManyToManyField(Sector)

    def __str__(self):
        return self.project_title


# models.signals.pre_save.connect(validate_project, sender=Project)