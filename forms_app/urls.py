from django.urls import path
from .views import contatti, lista_contatti, modifica_contatto, elimina_contatto

app_name='forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path("lista-contatti/", lista_contatti.as_view(), name="lista-contatti"),
    path('elimina-contatto/<int:pk>/', elimina_contatto, name='elimina-contatto'),
    path('modifica-contatto/<int:pk>/', modifica_contatto, name='modifica-contatto'),
]