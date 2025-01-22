from django.urls import path
from .views import home, articoloDetailView, lista_articoli, queryBase, giornalistaDetailView

app_name='news'

urlpatterns = [
    path('',home,name="homeview"),
    path("articoli/<int:pk>", articoloDetailView.as_view(), name="articolo_detail"),
    path("lista_articoli/", lista_articoli.as_view(), name="lista_articoli1"),
    path("lista_articoli/<int:pk>", lista_articoli.as_view(), name="lista_articoli"),
    path("queryBase/", queryBase, name="queryBase"),
    path("giornalista/<int:pk>", giornalistaDetailView.as_view(), name="giornalista_detail")
]
