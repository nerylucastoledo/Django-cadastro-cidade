from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cadastros.models import Cidade
from cadastros.serializers import CidadeSerializer


# class CidadeAPI(APIView):
#
#     def get(self, request, formt=None):
#
#         cidades = Cidade.objects.all()
#         serializer = CidadeSerializer(cidades, many=True)
#
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# class CidadeAPIList(ListAPIView):
#
#     queryset = Cidade.objects.all()
#     serializer_class = CidadeSerializer


class CidadeAPIList(ListCreateAPIView):

    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission = [permissions.IsAuthenticatedOrReadOnly]


# o primeiro é a criação da api na mão
# o segundo so da o get da api, ou seja, so mostra a api e os json
# o terceiro mostra a api e ainda da um formulario para criar mais cidade e etc, get e post