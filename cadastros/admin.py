from django.contrib import admin

# Register your models here.
from .models import Campo,Atividade

@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Atividade)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'pontos', 'detalhes')