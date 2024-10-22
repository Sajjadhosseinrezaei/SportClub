from django.shortcuts import render
from django.views import View
from players.models import Players


# Create your views here.
class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        players = Players.objects.all()
        return render(request, self.template_name, {'players': players})
