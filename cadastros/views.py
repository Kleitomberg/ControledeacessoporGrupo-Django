from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Atividade, Campo
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.

  ##CREATE VIEWS ##
class CreateCampo(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Campo
    fields = ['nome', 'descricao']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('login')

class CreateAtividade(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Atividade
    fields = ['titulo', 'numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('listar-Atividades')
    login_url = reverse_lazy('login')

    ##UPDATE VIEWS ##

class UpdateCampo(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Campo
    fields = ['nome', 'descricao']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('login')

class UpdateAtividade(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Atividade
    fields = ['titulo', 'numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('listar-Atividades')
    login_url = reverse_lazy('login')


  ##DELETE VIEWS ##

class DeleteCampo(GroupRequiredMixin, LoginRequiredMixin ,DeleteView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Campo    
    template_name='cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('login')

class DeleteAtividade(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Atividade
    template_name='cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-Atividades')
    login_url = reverse_lazy('login')

  ##LISTAR VIEWS ##

class ListCampo(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    login_url = reverse_lazy('login')

class ListAtividade(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"administrador", u"associacao", u"orgao"]
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
    login_url = reverse_lazy('login')