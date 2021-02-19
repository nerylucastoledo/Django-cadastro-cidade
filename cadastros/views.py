from django.shortcuts import render, get_object_or_404, redirect

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


def lista_cidades(request):
    qs = Cidade.objects.all().order_by('nome')

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


def cadastra_cidade(request):

    if request.method == 'POST':
        form = CidadeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cidades-list')

    else:

        form = CidadeForm()

    context = {
        'form': form
    }

    return render(request, 'cadastros/cadastra_cidades.html', context)


def remove_cidade(request, id):

    cidade = get_object_or_404(Cidade, pk=id)

    cidade.delete()

    return redirect('cidades-list')
