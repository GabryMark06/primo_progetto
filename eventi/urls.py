from django.urls import path
from .views import viewA, viewB, viewC, viewD

app_name='eventi'

urlpatterns = [
    
    path("viewA/", viewA.as_view(), name="viewA"),
    path("viewB/", viewB.as_view(), name="viewB"),
    path("viewC/", viewC, name="viewC"),
    path("viewD/", viewD.as_view(), name="viewD"),
    
]