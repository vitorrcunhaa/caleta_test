from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from billing.models import Game, Cash
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    games_queryset = Game.objects.filter(owner=request.user).all()
    games_dict = {}
    cash_queryset = Cash.objects.filter(owner=request.user).all()
    cash_dict = {}
    if games_queryset:
        for game in games_queryset:
            games_dict[game.name] = game.icon.url
        print(games_dict)
    if cash_dict:
        for cash in cash_dict:
            games_dict[game.name] = game.icon.url
        print(games_dict)
    return render(request, 'billing/index.html', {'games': games_dict})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


@csrf_exempt
def api_games_list(request):
    if request.user.is_authenticated:
        games = list(Game.objects.filter(owner=request.user).values())
        return JsonResponse(games, safe=False)
    else:
        return HttpResponse('You cannot access this API without logging in. <br> <a href="/accounts/login">Login</a>')


class GameList(ListView):
    model = Game

    def get_queryset(self):
        game = Game.objects.filter(owner=self.request.user)
        return game


class GameCreate(CreateView):
    model = Game
    fields = ['name', 'icon']
    success_url = reverse_lazy('game_list')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'icon']
    success_url = reverse_lazy('game_list')


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('game_list')
