from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Player, Tournament

# --- VIEW DA HOME PAGE ---
class HomePageView(TemplateView):
    template_name = 'home.html'

# --- VIEWS DE JOGADOR ---
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

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'apaga_jogador.html'
    success_url = reverse_lazy('lista-jogadores')

# --- VIEWS DE TORNEIO ---
class TournamentListView(ListView):
    model = Tournament
    template_name = 'lista_torneios.html'

class TournamentCreateView(CreateView):
    model = Tournament
    template_name = 'cria_torneio.html'
    fields = ['name']
    success_url = reverse_lazy('lista-torneios')

class TournamentUpdateView(UpdateView):
    model = Tournament
    template_name = 'edita_torneio.html'
    fields = ['name']
    success_url = reverse_lazy('lista-torneios')

class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'apaga_torneio.html'
    success_url = reverse_lazy('lista-torneios')