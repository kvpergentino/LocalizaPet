# core/admin.py
from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'status', 'especie', 'cidade', 'data_cadastro']
    list_display_links = ['id', 'nome']  # ID é clicável
    list_filter = ['status', 'especie', 'cidade']
    search_fields = ['id', 'nome', 'bairro', 'cidade']
    readonly_fields = ['id', 'data_cadastro', 'data_atualizacao']  # ID não editável