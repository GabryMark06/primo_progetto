from django.urls import path
from .views import home, articoloDetailView, lista_articoli, queryBase, giornalistaDetailView

app_name='news'

urlpatterns = [
    path('',home,name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/", lista_articoli, name="lista_articoli1"),
    path("lista_articoli/<int:pk>", lista_articoli, name="lista_articoli"),
    path("queryBase/", queryBase, name="queryBase"),
    path("giornalista/<int:pk>", articoloDetailView, name="giornalista_detail")
]
