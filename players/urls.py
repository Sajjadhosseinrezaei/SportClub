from django.urls import path
from . import views

app_name = 'players'


urlpatterns = [
    path('players_list', views.PlayersListView.as_view(), name='players_list'),

]
