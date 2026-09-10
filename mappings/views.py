from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )

    def perform_create(self, serializer):
        patient = serializer.validated_data["patient"]

        if patient.created_by != self.request.user:
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied(
                "You can only create mappings for your own patients."
            )

        serializer.save()


class MappingDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )


class PatientDoctorsView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]

        return PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            patient__created_by=self.request.user,
        )