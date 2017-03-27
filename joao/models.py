from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    evento = models.ForeignKey(EventoCientifico)

class Autor(Pessoa):
    curriculo = models.CharField(max_length=200)
    artigos = models.ManyToManyField(ArtigoCientifico)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=200)
    razaoSocial = models.CharField(max_length=200)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=200)

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    eventoPrincipal = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)
    dataEHoraDeInicio = models.DateField()
    palavrasChave = models.CharField(max_length=200)
    logotipo = models.CharField(max_length=200)
    realizador = models.ForeignKey(Pessoa)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)

class EventoCientifico(Evento):
    issn = models.CharField(max_length=200)
