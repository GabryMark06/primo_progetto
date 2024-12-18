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

def lista_articoli(request, pk=None):
    if(pk):
        articoli=Articolo.objects.filter(giornalista_id=pk)
        context={
            'articoli':articoli,
        }
        return render(request,'lista_articoli.html',context)
    else:
        articoli=Articolo.objects.all()
        context={
            'articoli':articoli,
        }
        return render(request,'lista_articoli_all.html',context)
    



