from rest_framework import generics
from .models import Planets
from .serializers import PlanetsSerializer

class PlanetsListCreateView(generics.ListCreateAPIView):
    queryset = Planets.objects.all()
    serializer_class = PlanetsSerializer

class PlanetsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planets.objects.all()
    serializer_class = PlanetsSerializer
