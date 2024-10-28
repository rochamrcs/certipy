from django.shortcuts import render
from .models import Participante 

def somar_cargas_horarias(cargas_horarias):
    total_horas = 0
    total_minutos = 0

    for carga in cargas_horarias:
        partes = carga.split(' e ')

        for parte in partes:
            parte = parte.strip() 
            if 'horas' in parte or 'h' in parte:
                try:
                    horas = int(parte.replace('horas', '').replace('h', '').strip())
                except ValueError:
                    horas = 0
                total_horas += horas
            
            if 'min' in parte or 'minutos' in parte:
                try:
                    minutos = int(parte.replace('min', '').replace('minutos', '').strip())
                except ValueError:
                    minutos = 0
                total_minutos += minutos

    total_horas += total_minutos // 60
    total_minutos = total_minutos % 60

    return total_horas, total_minutos

def home(request):
    participantes = []
    busca_realizada = False 
    total_horas = 0
    total_minutos = 0

    if request.method == "POST":
        email = request.POST.get('teste')
        participantes = Participante.objects.filter(email=email)
        busca_realizada = True 


        cargas_horarias = [p.carga_horaria for p in participantes]
        total_horas, total_minutos = somar_cargas_horarias(cargas_horarias)

    return render(request, 'home.html', {
        'participantes': participantes,
        'busca_realizada': busca_realizada,
        'total_horas': total_horas,
        'total_minutos': total_minutos,
    })

def certificados(request):
    # Este view precisa receber os dados do participante e horas total.
    # Supondo que você tenha uma lógica para obter esses dados.
    participantes = []  # Aqui você deve obter os dados de participantes relevantes
    total_horas = 0
    total_minutos = 0

    return render(request, 'certificado.html', {
        'participantes': participantes,
        'total_horas': total_horas,
        'total_minutos': total_minutos,
    })