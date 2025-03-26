from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Contatto
from django.shortcuts  import get_object_or_404,redirect

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required

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


@login_required(login_url='/accounts/login/')
def modifica_contatto(request, pk):
    # Preleva dal database l'oggetto la cui chiave primaria è passata come parametro
    contatto = get_object_or_404(Contatto, id=pk)

    """
    Se l'oggetto non viene trovato, get_object_or_404 restituisce una pagina di errore HTTP 404 (pagina non trovata).
    
    In Django, ci sono principalmente due tipi di richieste HTTP che una view può gestire: GET e POST.
    - Le richieste GET sono utilizzate per recuperare dati dal server,
    - Mentre le richieste POST sono utilizzate per inviare dati al server,
      ad esempio quando si invia un modulo HTML come in questo caso.
    """

    if request.method == "GET":
        # Prima chiamata GET per caricare il form
        form = FormContatto(instance=contatto)  # Al costruttore del form passo il contatto prelevato dal DB
    elif request.method == "POST":
        # Seconda chiamata POST per modificare il contatto
        form = FormContatto(request.POST, instance=contatto)  # Passo al form i dati modificati
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista-contatti')  # URL che reindirizza alla pagina lista_contatti.html

    context = {'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatto.html', context)



# Decoratore che permette di cancellare il contatto solo ad un utente admin
@staff_member_required(login_url='/accounts/login/')
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)

    if request.method == "POST":
        # Vuol dire che l'utente ha inviato il form che conferma l'eliminazione
        contatto.delete()  # Elimina il contatto dal database
        return redirect('forms_app:lista-contatti')

    context = {'contatto': contatto}
    return render(request, 'elimina_contatto.html', context)





