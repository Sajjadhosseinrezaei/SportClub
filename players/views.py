from django.shortcuts import render
from django.views.generic import ListView
from .models import Players
# Create your views here.


class PlayersListView(ListView):
    model = Players
    template_name = 'players/players_list.html'
    context_object_name = 'players'

