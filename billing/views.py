from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from billing.models import Game
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    games_queryset = Game.objects.all()
    games_dict = {}
    if games_queryset:
        for game in games_queryset:
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