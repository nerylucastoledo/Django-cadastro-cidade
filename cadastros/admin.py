from django.contrib import admin

from cadastros.models import Cidade, Estado, Pais

# registrando o model Cidade como admin
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Pais)