from django.urls import path
from . import views

urlpatterns = [
    path('', views.automated_documentation, name='automated_documentation'),
]
