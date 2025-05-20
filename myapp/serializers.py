from rest_framework import serializers
from .models import Planets

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ['id', 'name', 'population', 'terrains', 'climates']
