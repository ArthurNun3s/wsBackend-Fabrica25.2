from django.urls import path
from .views import PlayerListView, PlayerCreateView, PlayerUpdateView, HomePageView 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('players/', PlayerListView.as_view(), name='lista-jogadores'),

    path('players/new/', PlayerCreateView.as_view(), name='cria-jogador'),

    path('players/<int:pk>/edit/', PlayerUpdateView.as_view(), name='edita-jogador'),
]
