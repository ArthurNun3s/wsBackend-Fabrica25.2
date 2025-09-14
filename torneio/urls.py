from django.urls import path
from .views import ( HomePageView, PlayerListView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView, TournamentListView, TournamentCreateView, TournamentUpdateView, TournamentDeleteView )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('players/', PlayerListView.as_view(), name='lista-jogadores'),

    path('players/new/', PlayerCreateView.as_view(), name='cria-jogador'),

    path('players/<int:pk>/edit/', PlayerUpdateView.as_view(), name='edita-jogador'),
    
    path('players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='apaga-jogador'),

    path('tournaments/', TournamentListView.as_view(), name='lista-torneios'),

    path('tournaments/new/', TournamentCreateView.as_view(), name='cria-torneio'),

    path('tournaments/<int:pk>/edit/', TournamentUpdateView.as_view(), name='edita-torneio'),

    path('tournaments/<int:pk>/delete/', TournamentDeleteView.as_view(), name='apaga-torneio'),

]