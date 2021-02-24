from django.contrib.auth.decorators import login_required
from django.urls import path

from cadastros.views import CidadeList, CidadeDetail, CidadeDelete, CidadeCreate, CidadeUpdate, EstadoList, \
    EstadoCreate, EstadoDelete, EstadoDetail

urlpatterns = [
    path('', CidadeList.as_view(), name="cidades-list"),
    path('estados/', EstadoList.as_view(), name="estados-list"),

    path('detalhe/<int:pk>/', CidadeDetail.as_view(), name="cidades-detalhe"),
    path('estados/detalhe/<int:pk>/', EstadoDetail.as_view(), name="estados-detalhe"),

    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name="cidades-remove"),
    path('estados/delete/<int:pk>/', login_required(EstadoDelete.as_view()), name="estados-remove"),

    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name="cidades-editar"),

    path('create/', login_required(CidadeCreate.as_view()), name="cidade-cadastro"),
    path('estados/create', login_required(EstadoCreate.as_view()), name="estado-cadastro"),
]