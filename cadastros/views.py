from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.forms import CidadeForm, EstadoForm
from cadastros.models import Cidade, Estado

class BaseListView(ListView):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cidades'
        return context

class EstadoList(BaseListView):

    queryset = Estado.objects.all().order_by('nome')
    context_object_name = 'estados'
    template_name = 'cadastros/lista_estados.html'


class EstadoDetail(DetailView):

    queryset = Estado.objects.all()
    context_object_name = 'estado'
    template_name = 'cadastros/detalhe_estados.html'


class EstadoCreate(CreateView):

    model = Estado
    form_class = EstadoForm
    success_url = reverse_lazy('estados-list')
    template_name = 'cadastros/cadastra_estados.html'


class EstadoDelete(DeleteView):

    model = Estado
    template_name = 'cadastros/remove_estados.html'
    context_object_name = 'estado'
    success_url = reverse_lazy('estados-list')


class CidadeList(BaseListView):

    # model = Cidade
    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):

    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):

    model = Cidade
    template_name = 'cadastros/cadastra_cidades.html'
    form_class = CidadeForm
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):

    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadastro atualizado com sucesso!'


    # caso queira usar um form pronto do django, so n por o form_class a cima e nem o fields

# class CidadeList(View):
#
#     def get(self, request):
#         qs = Cidade.objects.all().order_by('nome')
#
#         context = {
#             'cidades': qs,
#             'titulo': 'cidades'
#         }
#
#         return render(request, 'cadastros/lista_cidades.html', context)

# def lista_cidades(request):
#     qs = Cidade.objects.all().order_by('nome')
#
#     context = {
#             'cidades': qs,
#             'titulo': 'cidades'
#         }
#
#     return render(request, 'cadastros/lista_cidades.html', context)

# def detalhe_cidade(request, id):
#     # tenta pegar o objeto ou retorna o erro 404
#     # ex: cidade = Cidade.objects.get
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     context = {
#         'cidade': cidade
#     }
#
#     return render(request, 'cadastros/detalhe_cidades.html', context)

# def cadastra_cidade(request):
#
#     if request.method == 'POST':
#         form = CidadeForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#
#     else:
#
#         form = CidadeForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'cadastros/cadastra_cidades.html', context)

# @login_required
# def remove_cidade(request, id):
#
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     cidade.delete()
#
#     return redirect('cidades-list')

# @login_required
# def editar_cidade(request, id):
#
#     cidade_obj = get_object_or_404(Cidade, pk=id)
#     form = CidadeForm(request.POST or None, instance=cidade_obj)
#
#     # receber os dados da cidade e apresentar
#     if request.method == 'Post':
#         form = CidadeForm(request.POST, instance=cidade_obj)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('cidades-list')
#
#     context = {
#         'form': form,
#         'obj': cidade_obj
#     }
#
#     return render(request, 'cadastros/edita_cidades.html', context)


# def cadastra_estado(request):
#
#     if request.method == 'POST':
#         form = EstadoForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('estados-list')
#
#     else:
#         form = EstadoForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'cadastros/cadastra_estados.html', context)

# def remove_estado(request, id):
#
#     estado = get_object_or_404(Estado, pk=id)
#
#     estado.delete()
#
#     return redirect('estados-list')

# def detalhe_estado(request, id):
#
#     estado = get_object_or_404(Estado, pk=id)
#
#     context = {
#         'estado': estado
#     }
#
#     return render(request, 'cadastros/detalhe_estados.html', context)
