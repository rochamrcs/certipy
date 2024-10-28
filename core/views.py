from django.shortcuts import render
from .models import Participante 

def home(request):
    participantes = []
    busca_realizada = False 

    if request.method == "POST":
        email = request.POST.get('teste')
        participantes = Participante.objects.filter(email=email)
        busca_realizada = True 

    return render(request, 'home.html', {
        'participantes': participantes,
        'busca_realizada': busca_realizada,
    })
