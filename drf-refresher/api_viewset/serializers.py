from rest_framework import serializers
from .models import Doctors

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'doctor_id', 'name', 'specialty']
        read_only_fields = ['id']