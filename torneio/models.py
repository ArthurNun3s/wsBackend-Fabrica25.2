# Em torneio/models.py

from django.db import models
from django.utils import timezone

class Player(models.Model):
    name = models.CharField(max_length=100)
    
    character = models.CharField(max_length=50, help_text="Ex: Scorpion, Shunsui, Ryu")

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='matches', on_delete=models.CASCADE)
    round_number = models.PositiveIntegerField(help_text="Ex: 1 para Oitavas, 2 para Quartas...")
    player1 = models.ForeignKey(Player, related_name='matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='matches_as_player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='matches_won', on_delete=models.SET_NULL, null=True, blank=True)
    match_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Round {self.round_number}: {self.player1} vs {self.player2} in {self.tournament.name}"

