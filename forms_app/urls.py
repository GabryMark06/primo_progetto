from django.urls import path
from .views import contatti, lista_contatti

app_name='forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path("lista_contatti/", lista_contatti.as_view(), name="lista_contatti"),
]