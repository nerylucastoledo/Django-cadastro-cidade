from django.shortcuts import render

from cadastros.models import Cidade


def lista_cidades(request):

    qs = Cidade.objects.all()
    qs_capitais = Cidade.objects.all().filter(capital=True)