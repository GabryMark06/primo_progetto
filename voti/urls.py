from django.urls import path
from .views import viewA, viewB, viewC, viewD

app_name='voti'

urlpatterns = [
    path("viewA/", viewA, name="viewA"),
    path("viewB/", viewB, name="viewB"),
    path("viewC/", viewC, name="viewC"),
    path("viewD/", viewD, name="viewD"),
]