from django.contrib import admin
from .models import Cash


class CashAdmin(admin.ModelAdmin):
    fields = ['owner', 'field', 'value']
    list_display = ('owner', 'field', 'value')


admin.site.register(Cash, CashAdmin)
