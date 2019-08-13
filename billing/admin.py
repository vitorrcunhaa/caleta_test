from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    fields = ['owner', 'name', 'icon']
    list_display = ('owner', 'name', 'icon')


admin.site.register(Game, GameAdmin)
