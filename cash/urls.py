from django.contrib.auth.decorators import login_required
from django.urls import path

from cash import views

urlpatterns = [
    path('api/cash_list', login_required(views.api_cash_list), name='api_cash_list'),
    path('cash_list', login_required(views.CashList.as_view()), name='cash_list'),
    path('cash_new', login_required(views.CashCreate.as_view()), name='cash_new'),
    path('cash_edit/<int:pk>/', login_required(views.CashUpdate.as_view()), name='cash_edit'),
    path('cash_delete/<int:pk>/', login_required(views.CashDelete.as_view()), name='cash_delete'),
]
