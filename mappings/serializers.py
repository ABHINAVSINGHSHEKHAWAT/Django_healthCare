from rest_framework import serializers

from .models import PatientDoctorMapping


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "doctor",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, data):
        patient = data.get("patient")
        doctor = data.get("doctor")

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return data