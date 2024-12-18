from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli":articoli,"giornalisti":giornalisti}
    print(context)
    return render(request,"homepage_news.html",context)

def articoloDetailView(request, pk):
    articolo=get_object_or_404(Articolo, pk=pk)
    context={"articolo":articolo}
    return render(request,"articolo_detail.html",context)



