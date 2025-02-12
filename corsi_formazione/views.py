from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import datetime
from .models import Corso

def indexC(request):
    return render(request,"indexC.html")

class viewA1(ListView):

    model = Corso
    template_name = "viewA1.html"
    context_object_name = "corsi"  
    ordering = ['data_inizio']

class viewB1(DetailView):
    model=Corso
    template_name="viewB1.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["corso"] = Corso.objects.get(id=pk)
        return context
    
class viewC1(ListView):
    model = Corso
    template_name = "viewC1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(data_inizio__gt=(datetime.date(2025,5,1)))
        return context
    
class viewD1(ListView):
    model=Corso
    template_name="viewD1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(posti_disponibili__lt=20)
        return context

class viewE1(ListView):
    model = Corso
    template_name = "viewE1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(data_inizio__lt=(datetime.date(2025,4,30)))
        return context
    
class viewF1(ListView):
    model = Corso
    template_name = "viewF1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsoMax"] = Corso.objects.order_by('-posti_disponibili').first()
        context["corsoMin"] = Corso.objects.order_by('posti_disponibili').first()
        allCorsi= Corso.objects.all()
        tot=0
        for corso in allCorsi:
            tot+=corso.posti_disponibili
        context["posti_disponibili"]=tot
        return context