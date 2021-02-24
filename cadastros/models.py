from django.db import models


# criando um model/class chamado Cidade (tabela)

class Pais(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Estado(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Cidade(models.Model):
    # criação dos campos que Cidade irá conter

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True, blank=False)
    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome