# Em torneio/serializers.py

from rest_framework import serializers
from .models import Player, Tournament, Match

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'character']

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'start_date']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'tournament', 'round_number', 'player1', 'player2', 'winner', 'match_date']