from django.contrib import admin
from pets.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'status', 'especie', 'cidade', 'uf', 'usuario']
    list_display_links = ['id', 'nome']
    list_filter = ['status', 'especie', 'uf']
    search_fields = ['nome', 'bairro', 'cidade', 'cep']
    readonly_fields = ['id']