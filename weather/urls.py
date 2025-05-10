from django.urls import path, include
from django.views.generic import TemplateView
from .views import WeatherView

urlpatterns = [
    path('', WeatherView.as_view(), name='weather'),
]