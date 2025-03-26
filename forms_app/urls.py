from django.urls import path
from .views import contatti, lista_contatti, modifica_contatto, elimina_contatto

app_name='forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path("lista_contatti/", lista_contatti.as_view(), name="lista_contatti"),
    path('elimina_contatto/', elimina_contatto, name='elimina-contatto'),
    path('modifica_contatto/', modifica_contatto, name='modifica-contatto'),
]