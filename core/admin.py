from django.contrib import admin
from .models import Participante, Documento


class ParticipanteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'email', 'curso']
    list_display = ['order', 'nome', 'email', 'curso', 'carga_horaria'] 
    ordering = ['order'] 


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    search_fields = ('titulo',)
    list_filter = ('data_criacao',)


admin.site.register(Participante, ParticipanteAdmin)
