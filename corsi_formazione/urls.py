from django.urls import path
from .views import indexC, viewA1, viewB1, viewC1, viewD1, viewE1, viewF1

app_name='corsi_formazione'

urlpatterns = [
    path('',indexC,name="indexC"),
    path("viewB1/<int:pk>", viewB1.as_view(), name="viewB1"),
    path("viewA1/", viewA1.as_view(), name="viewA1"),
    path("viewC1/", viewC1.as_view(), name="viewC1"),
    path("viewD1/", viewD1.as_view(), name="viewD1"),
    path("viewE1/", viewE1.as_view(), name="viewE1"),
    path("viewF1/", viewF1.as_view(), name="viewF1")
]