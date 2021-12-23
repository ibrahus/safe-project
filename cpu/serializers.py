from django.db.models import fields
from rest_framework import serializers
from .models import CPU


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ['id', 'name', 'cors', 'speed']
