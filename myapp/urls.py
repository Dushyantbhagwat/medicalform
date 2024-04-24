from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("doctor/", views.doctor, name='doctor'),
    path("patient/", views.patient, name='patient'),
    path("appointment/", views.appointment, name='appointment'),
]

