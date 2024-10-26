from django.shortcuts import render
from .models import Participante

def home(request):
    email = request.GET.get('email')
    participante = None
    cursos = []

    if email:
        try:
            participante = Participante.objects.get(email=email)
            cursos = participante.curso.all()
        except Participante.DoesNotExist:
            participante = None

    return render(request, './home.html', {'participante': participante, 'cursos': cursos, 'email': email})
