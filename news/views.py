from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista
import datetime

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

def queryBase(request):
    articoli_cognome=Articolo.objects.filter(giornalista_cognome="Rossi")
    
    numero_totale_articoli=Articolo.objects.count()

    giornalista1=Giornalista.objects.get(id=1)
    nArticoli_giornalista1=Articolo.objects.filter(giornalista=giornalista1).count()

    articoli_ordinati=Articolo.objects.order_by("-visualizzazioni")
    
    articoli_senza_visualizzazioni=Articolo.objects.filter(visualizzazioni=0)
    
    articolo_maxVis=articoli_ordinati.first()
    
    giornalisti_data=Giornalista.objects.filter(anno_di_nascita__gt=datetime.data(1990,1,1))
    
    articoli_del_giorno=Articolo.objects.filter(data=datetime.data(2023,1,1))
    
    articolo_periodo=Articolo.objects.filter(date__range=(datetime.data(2023,1,1), datetime.data(2023,12,31)))
    
    giornalisti_nati=Giornalista.objects.filter(anno_di_nascita__lt=datetime.data(1980,1,1))
    articoli_giornalisti=Giornalista.objects.filter(giornalista__in=giornalisti_nati)
    
    giornalista_giovane=Giornalista.objects.order_by('anno_di_nascita').first()
    
    giornalista_anziano=Giornalista.objects.order_by('-anno_di_nascita').first()
    
    ultimi=Articolo.objects.order_by('-data')[:5]
    
    articolo_min_vis=Articolo.objects.filter(visualizzazioni__gte=100)
    
    articoli_parola=Articolo.objects.filter(titolo__icontains='importante')
    context={
        'articoli_cognome':articoli_cognome,
        'numero_totale_articoli':numero_totale_articoli,
        'mArticoli_giornalista1':nArticoli_giornalista1,
        'articoli_senza_visualizzazioni':articoli_senza_visualizzazioni,
        'articolo_max_vis':articolo_maxVis,
        'giornalisti_data':giornalisti_data,
        'articoli_del_giorno':articoli_del_giorno,
        'articolo_periodo':articolo_periodo,
        'articoli_giornalisti':articoli_giornalisti,
        'giornalista_giovane':giornalista_giovane,
        'giornalista_anziano':giornalista_anziano,
        'ultimi':ultimi,
        'articolo_min_vis':articolo_min_vis,
        'articoli_parola':articoli_parola
    }
    return render(request,'query.html',context)




