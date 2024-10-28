from django.db import models


class Participante(models.Model):
    order = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ingresso = models.CharField(max_length=50)
    curso = models.CharField(max_length=255)
    carga_horaria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='pdfs/')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo