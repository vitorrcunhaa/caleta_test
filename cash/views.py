from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from cash.models import Cash
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@csrf_exempt
def api_cash_list(request):
    cashs = list(Cash.objects.filter(owner=request.user).values())
    return JsonResponse(cashs, safe=False)


class CashList(ListView):
    model = Cash

    def get_queryset(self):
        cash = Cash.objects.filter(owner=self.request.user)
        return cash


class CashCreate(CreateView):
    model = Cash
    fields = ['field', 'value']
    success_url = reverse_lazy('cash_list')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CashCreate, self).get_context_data(**kwargs)
        context['is_create'] = True
        return context


class CashUpdate(UpdateView):
    model = Cash
    fields = ['field', 'value']
    success_url = reverse_lazy('cash_list')

    def get_context_data(self, **kwargs):
        context = super(CashUpdate, self).get_context_data(**kwargs)
        context['is_create'] = False
        return context


class CashDelete(DeleteView):
    model = Cash
    success_url = reverse_lazy('cash_list')
