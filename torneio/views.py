from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.conf import settings 
import requests 
from .models import Player, Tournament
from .forms import TournamentForm
import random
from django.shortcuts import redirect
from .models import Player, Tournament, Match

# --- VIEW DA HOME PAGE ---
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            
            api_key = settings.RAWG_API_KEY
            
            url = f"https://api.rawg.io/api/games?key={api_key}&ordering=-rating&page_size=3"
            
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()
            context['games'] = data.get('results', [])
        except requests.exceptions.RequestException as e:
            context['api_error'] = 'Não foi possível buscar os jogos no momento.'
            print(f"Erro ao buscar da API RAWG: {e}")
            
        return context

# --- VIEWS DE JOGADOR ---
class PlayerListView(ListView):
    model = Player
    template_name = 'lista_jogadores.html'

class PlayerCreateView(CreateView):
    model = Player
    template_name = 'cria_jogador.html'
    fields = ['name', 'character']
    success_url = reverse_lazy('lista-jogadores')

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'edita_jogador.html'
    fields = ['name', 'character']
    success_url = reverse_lazy('lista-jogadores')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'apaga_jogador.html'
    success_url = reverse_lazy('lista-jogadores')

# --- VIEWS DE TORNEIO ---
class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'detalhes_torneio.html'


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
    form_class = TournamentForm
    success_url = reverse_lazy('lista-torneios')

class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'apaga_torneio.html'
    success_url = reverse_lazy('lista-torneios')

# --- LÓGICA DO CHAVEAMENTO ---
def gerar_chaveamento(request, pk):
    if request.method == 'POST':
        torneio = Tournament.objects.get(pk=pk)
        jogadores = list(torneio.players.all())
        
        random.shuffle(jogadores)
        
        Match.objects.filter(tournament=torneio, round_number=1).delete()

        for i in range(0, len(jogadores) - 1, 2):
            jogador1 = jogadores[i]
            jogador2 = jogadores[i+1]
            Match.objects.create(
                tournament=torneio,
                player1=jogador1,
                player2=jogador2,
                round_number=1
            )
            
    return redirect('detalhes-torneio', pk=torneio.pk)

