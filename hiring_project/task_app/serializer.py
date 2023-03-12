from rest_framework import serializers
from .models import *
import csv
import logging


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

    # def validate(self, value):
    #     return value

    # def create(self, validate_data):
    #     try:
    #         print(validate_data)
    #         obj, created = District.objects.get_or_create(
    #             name="temp", defaults={"district_name": validate_data["District"]})
    #     except Exception as e:
    #         raise e


# class CSVFileSerializer(serializers.Serializer):
#     csv_file = serializers.FileField()

#     def validate_csv_file(self, value):
#         logging.basicConfig(filename="example.log", level=logging.DEBUG)

#         if not value.name.endswith(".csv"):
#             raise serializers.ValidationError("File is not csv")

#         data = []
#         logging.debug("here")
#         decoded_file = value.read().decode('utf-8').splitlines()
#         logging.debug("here 1", decoded_file)
#         reader = csv.DictReader(decoded_file)
#         header = next(reader)

#         for row in reader:
#             row_data = {}
#             for i, val in enumerate(row):
#                 row_data[header[i]] = val

#             data.append(row_data)

#         return data

#     def create(self, validate_data):
#         for row in validate_data:
#             print(row)
