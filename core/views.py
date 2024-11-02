from django.shortcuts import render
from .models import Participante 
from django.db.models import Case, When, Value, IntegerField

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
    carga_palestras = 0

    if request.method == "POST":
        email = request.POST.get('teste')
        # Ordena para que "Tutoriais" venham antes de "Palestras"
        participantes = Participante.objects.filter(email=email).annotate(
            curso_priority=Case(
                When(curso="Tutoriais", then=Value(1)),   # Prioridade 1 para Tutoriais
                When(curso="Palestras", then=Value(2)),   # Prioridade 2 para Palestras
                default=Value(3),                         # Outras categorias terão prioridade 3
                output_field=IntegerField()
            )
        ).order_by('curso_priority', 'curso')  # Ordena por prioridade e pelo nome do curso

        busca_realizada = True 
        tipo = []

        for participante in participantes:
            participante.is_palestrante = (participante.ingresso == "Palestrante")
            if participante.is_palestrante:
                tipo.append("Palestrante")
            else:
                pass

        cargas_horarias = [p.carga_horaria for p in participantes]
        total_horas, total_minutos = somar_cargas_horarias(cargas_horarias)

        if "Palestrante" in tipo:
            total_horas -= 1
            total_minutos = 30
            carga_palestras = "13 horas"
        else:
            carga_palestras = "13 horas e 30 minutos"
        
        print(carga_palestras)

        # Armazenar dados na sessão
        request.session['participantes'] = list(participantes.values())
        request.session['total_horas'] = total_horas
        request.session['total_minutos'] = total_minutos
        request.session['carga_palestras'] = carga_palestras

    return render(request, 'home.html', {
        'participantes': participantes,
        'busca_realizada': busca_realizada,
        'total_horas': total_horas,
        'total_minutos': total_minutos,
        'carga_palestras': carga_palestras
    })

def certificados(request):
    # Recuperar os dados da sessão
    participantes = request.session.get('participantes', [])
    total_horas = request.session.get('total_horas', 0)
    total_minutos = request.session.get('total_minutos', 0)
    carga_palestras = request.session.get('carga_palestras', 0)

    return render(request, 'certificado.html', {
        'participantes': participantes,
        'total_horas': total_horas,
        'total_minutos': total_minutos,
        'carga_palestras': carga_palestras
    })