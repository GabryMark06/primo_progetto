from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import datetime
from .models import Evento

class viewA(ListView):

    model=Evento
    template_name="viewA.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["eventi"] = Evento.objects.all().order_by('data_evento')
        return context
    
class viewB(ListView):
    model = Evento
    template_name = "viewB.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["eventi"] = Evento.objects.all()
        return context

class viewD(ListView):
    model=Evento
    template_name="viewD.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["eventoMax"] = Evento.objects.order_by('-partecipanti').first()
        context["eventoMin"] = Evento.objects.order_by('partecipanti').first()
        return context
    
def viewC(request):
    totPartecipanti=Evento.objects.all().values_list('partecipanti', flat=True)
    somma=sum(totPartecipanti)
    media=somma/(Evento.objects.count())
    context={
        'somma': somma,
        'media':media
    }
    return render(request,'viewC.html',context)

# Create your views here.
