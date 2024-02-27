from rest_framework import serializers
from hospital.models import Doctor, Patient

class DoctorSerializer(serializers.Serializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.Serializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"