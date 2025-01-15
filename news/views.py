from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista
import datetime
from django.db.models import Q

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
    articoli_cognome=Articolo.objects.filter(giornalista__cognome="Rossi")
    
    numero_totale_articoli=Articolo.objects.count()

    giornalista1=Giornalista.objects.get(id=1)
    nArticoli_giornalista1=Articolo.objects.filter(giornalista=giornalista1).count()

    articoli_ordinati=Articolo.objects.order_by("-visualizzazioni")
    
    articoli_senza_visualizzazioni=Articolo.objects.filter(visualizzazioni=0)
    
    articolo_maxVis=Articolo.objects.order_by("-visualizzazioni").first()
    
    giornalisti_data=Giornalista.objects.filter(anno_nascita__gt=datetime.date(1990,1,1))
    
    articoli_del_giorno=Articolo.objects.filter(data_articolo=datetime.date(2023,1,1))
    
    articolo_periodo=Articolo.objects.filter(data_articolo__range=(datetime.date(2023,1,1), datetime.date(2023,12,31)))
    
    giornalisti_nati=Giornalista.objects.filter(anno_nascita__lt=datetime.date(1980,1,1))
    articoli_giornalisti=Articolo.objects.filter(giornalista__in=giornalisti_nati)
    
    giornalista_giovane=Giornalista.objects.order_by('anno_nascita').first()
    
    giornalista_anziano=Giornalista.objects.order_by('-anno_nascita').first()
    
    ultimi=Articolo.objects.order_by('-data_articolo')[:5]
    
    articolo_min_vis=Articolo.objects.filter(visualizzazioni__gte=100)
    
    articoli_parola=Articolo.objects.filter(titolo__icontains='importante')

    articoli_mese_anno=Articolo.objects.filter(data_articolo__month=1, data_articolo__year=2023)

    giornalisti_con_articoli_popolari=Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()

    data1=datetime.date(1990,1,1)
    visualizzazioni1=50

    articoli_con_and=Articolo.objects.filter(giornalista__anno_nascita__gt=data1, visualizzazioni__gte=visualizzazioni1)

    
    articoli_con_or=Articolo.objects.filter(Q(giornalista__anno_nascita__gt=data1) | Q(visualizzazioni__lte=visualizzazioni1))


    articoli_con_not=Articolo.objects.filter(~Q(giornalista__anno_nascita__lt=data1))

    articoli_con_not=Articolo.objects.exclude(giornalista__anno_nascita__lt=data1)

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
        'articoli_parola':articoli_parola,
        'articoli_mese_anno':articoli_mese_anno,
        'giornalisti_con_articoli_popolari':giornalisti_con_articoli_popolari,
        'articoli_con_and':articoli_con_and,
        'articoli_con_or':articoli_con_or,
        'articoli_con_not':articoli_con_not
    }
    return render(request,'query.html',context)

def giornalistaDetailView(request, pk):
    giornalista=get_object_or_404(Giornalista,pk=pk)
    context={"giornalista":giornalista}
    return render(request, "giornalista_detail.html", context)




