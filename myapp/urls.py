from django.urls import path
from .views import PlanetsListCreateView, PlanetsView

urlpatterns = [
    path('planets/', PlanetsListCreateView.as_view(), name='planets-list-create'),
    path('planets/<int:pk>/', PlanetsView.as_view(), name='planets-detail'),
]
