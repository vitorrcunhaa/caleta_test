from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game_list', views.GameList.as_view(), name='game_list'),
    path('game_new', views.GameCreate.as_view(), name='game_new'),
    path('game_edit/<int:pk>/', views.GameUpdate.as_view(), name='game_edit'),
    path('game_delete/<int:pk>/', views.GameDelete.as_view(), name='game_delete'),
]
