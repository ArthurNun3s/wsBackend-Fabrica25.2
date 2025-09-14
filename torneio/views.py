from django.views.generic import ListView, CreateView, UpdateView, TemplateView 
from django.urls import reverse_lazy
from .models import Player

class HomePageView(TemplateView):
    template_name = 'home.html'

class PlayerListView(ListView):
    model = Player
    template_name = 'lista_jogadores.html'

class PlayerCreateView(CreateView):
    model = Player
    template_name = 'cria_jogador.html'
    fields = ['name', 'role', 'character']
    success_url = reverse_lazy('lista-jogadores')

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'edita_jogador.html' 
    fields = ['name', 'role', 'character']
    success_url = reverse_lazy('lista-jogadores')