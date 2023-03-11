from django.db import models


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=255)

    def __str__(self):
        return self.province_name


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name


class Municipality(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    municipality_name = models.CharField(max_length=255)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipality_name


class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    donor_name = models.CharField(max_length=500)

    def __str__(self):
        return self.donor_name


class ExecutingAgency(models.Model):
    executing_agency_id = models.AutoField(primary_key=True)
    executing_agency_name = models.CharField(max_length=500)

    def __str__(self):
        return self.executing_agency_name


class ImplementingPartner(models.Model):
    implementing_partner_id = models.AutoField(primary_key=True)
    implementing_partner_name = models.CharField(max_length=500)

    def __str__(self):
        return self.implementing_partner_name


class CounterpartMinistry(models.Model):
    counterpart_ministry_id = models.AutoField(primary_key=True)
    counterpart_ministry_name = models.CharField(max_length=500)

    def __str__(self):
        return self.counterpart_ministry_name


class Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=255)

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
        max_length=6, choices=TYPE_OF_ASSISTANCE_CHOICES)

    def __str__(self):
        return self.type_of_assistance


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
    municipality_id = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title


class ProjectTypeOfAssistance(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    type_of_assistance_id = models.ForeignKey(
        TypeOfAssistance, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, primary_key=True)


class ProjectExecutingAgency(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    executing_agency_id = models.ForeignKey(
        ExecutingAgency, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, primary_key=True)


class ProjectImplementingPartner(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    implementing_partnet_id = models.ForeignKey(
        ImplementingPartner, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, primary_key=True)


class ProjectSector(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    sector_id = models.ForeignKey(Sector, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, primary_key=True)


class Agreement(models.Model):
    agreement_id = models.AutoField(primary_key=True)
    agreement_date = models.DateField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    executing_agency_id = models.ForeignKey(
        ExecutingAgency, on_delete=models.CASCADE)
    sector_id = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agreement_date}"


class CommitmentDisbursement(models.Model):
    commitment_disbursement_id = models.AutoField(primary_key=True)
    commitment = models.IntegerField()
    disbursement = models.FloatField()
    agreement_id = models.ForeignKey(Agreement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.commitment} | {self.disbursement}"
