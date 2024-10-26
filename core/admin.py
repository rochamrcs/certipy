from django.contrib import admin
from .models import Participante


class ParticipanteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'email', 'curso']
    list_display = ['order', 'nome', 'email', 'curso', 'carga_horaria'] 
    ordering = ['order'] 

admin.site.register(Participante, ParticipanteAdmin)
