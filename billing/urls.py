from django.contrib.auth.decorators import login_required
from django.urls import path

from billing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/games_list', login_required(views.api_games_list), name='api_games_list'),
    path('game_list', login_required(views.GameList.as_view()), name='game_list'),
    path('game_new', login_required(views.GameCreate.as_view()), name='game_new'),
    path('game_edit/<int:pk>/', login_required(views.GameUpdate.as_view()), name='game_edit'),
    path('game_delete/<int:pk>/', login_required(views.GameDelete.as_view()), name='game_delete'),
]
