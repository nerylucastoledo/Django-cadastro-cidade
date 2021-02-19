from django.shortcuts import render, get_object_or_404

from cadastros.models import Cidade


def lista_cidades(request):

    qs = Cidade.objects.all()

    context = {
        'cidades': qs,
        'titulo': 'cadastro de cidades'
    }

    return render(request, 'cadastros/lista_cidades.html', context)


def detalhe_cidade(request, id):

    # tenta pegar o objeto ou retorna o erro 404
    # ex: cidade = Cidade.objects.get
    cidade = get_object_or_404(Cidade, pk=id)

    context = {
        'cidade': cidade
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)