from django.http import HttpResponse
from django.shortcuts import render

from reviste.models import Revista, Publicatie


# Create your views here.
def hello_reviste(request):
    return HttpResponse('Pagina de reviste.')

def reviste(request):
    reviste = Revista.objects.all()
    publicatii = Publicatie.objects.all()

    return render(
        request,
        template_name='reviste.html',
        context={'reviste': reviste, 'publicatii': publicatii}
    )

def reviste_detail(request, title):
    revista = Revista.objects.get(title=title)

    return render(
        request,
        template_name='reviste_detail.html',
        context={'revista': revista}
    )