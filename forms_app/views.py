from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Contatto

def contatti(request):
    form=FormContatto()
    context={"form": form}
    return render(request, "contatto.html", context)


def contatti(request):

    if request.method == "POST":

        form = FormContatto(request.POST)

        if form.is_valid():
            print("Il Form è Valido!")
            print("NOME:", form.cleaned_data["nome"])
            print("COGNOME:", form.cleaned_data["cognome"])
            print("EMAIL:", form.cleaned_data["email"])
            print("CONTENUTO:", form.cleaned_data["contenuto"])
            print("Salvo il contatto nel database")
            nuovo_contatto=form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    else:
        form = FormContatto()
    context = {"form": form}
    return render(request, "contatto.html", context)

class lista_contatti(ListView):

    model = Contatto
    template_name = "lista_contatti.html"
    context_object_name = "contatti" 






