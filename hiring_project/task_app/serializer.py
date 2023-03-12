from rest_framework import serializers
from .models import *


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = District
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = Municipality
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'


class ExecutingAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutingAgency
        fields = '__all__'


class ImplementingPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImplementingPartner
        fields = '__all__'


class CounterpartMinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterpartMinistry
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class TypeOfAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfAssistance
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class CommitmentDisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitmentDisbursement
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    municipality = MunicipalitySerializer()
    agreement = AgreementSerializer()
    commitment_disbursement = CommitmentDisbursementSerializer()
    donor = DonorSerializer()
    executing_agency = ExecutingAgencySerializer(many=True)
    implementing_partner = ImplementingPartnerSerializer(many=True)
    project_sector = SectorSerializer(many=True)
    type_of_assistance = TypeOfAssistanceSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
