from django.contrib import admin

from cadastros.models import Cidade

# registrando o model Cidade como admin
admin.site.register(Cidade)