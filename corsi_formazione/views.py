from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
import datetime
from .models import Corso

def indexC(request):
    return render(request,"indexC.html")

class viewA1(ListView): #con l' utilizzo dela classe ListView ordino i corsi in ordine crescente in base alla data di inizio

    model = Corso
    template_name = "viewA1.html"
    context_object_name = "corsi"  
    ordering = ['data_inizio']

class viewB1(DetailView): #con l' utilizzo dela classe DetailView prendo l' id passato dalla pagina viewA.html per fare un dettaglio del corso
    model=Corso
    template_name="viewB1.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["corso"] = Corso.objects.get(id=pk)
        return context
    
class viewC1(ListView): #con l' utilizzo dela classe ListView prende i corsi iniziati dopo la data riportata
    model = Corso
    template_name = "viewC1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(data_inizio__gt=(datetime.date(2025,5,1)))
        return context
    
class viewD1(ListView): #con l' utilizzo dela classe ListView restituisco i corsi con meno di 20 posti disponibili
    model=Corso
    template_name="viewD1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(posti_disponibili__lte=20)
        return context

class viewE1(ListView): #con l' utilizzo dela classe ListView restituisco i corsi che finiscono prima della data riportata
    model = Corso
    template_name = "viewE1.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["corsi"] = Corso.objects.filter(data_inizio__lt=(datetime.date(2025,4,30)))
        return context
    
class viewF1(ListView): #con l' utilizzo dela classe ListView restituisco i corsi con max posti disponibili, min posti disponibili e totale posti disponibili
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