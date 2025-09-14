# em torneio/forms.py
from django import forms
from .models import Tournament, Player

class TournamentForm(forms.ModelForm):
    # Isso transforma a seleção de jogadores em checkboxes, que é mais amigável
    players = forms.ModelMultipleChoiceField(
        queryset=Player.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Tournament
        fields = ['name', 'players']