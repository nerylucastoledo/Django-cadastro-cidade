from django.db import models

# criando um model/class chamado Cidade (tabela)
class Cidade(models.Model):

    #criação dos campos que Cidade irá conter
    nome = models.CharField(max_length=100)
    capital = models.BooleanField(default=False)

    def __str__(self):

        return self.nome
