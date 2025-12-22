from django.urls import path
from . import views

urlpatterns = [
    path('', views.agents, name='agents'),
    path('create/', views.agents_create, name='agents_create'),
    path('<int:agent_id>/edit/', views.agents_edit, name='agents_edit'),

]
