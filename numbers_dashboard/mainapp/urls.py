from django.contrib import admin
from django.urls import path

from .views import OrdersView
from .views import OrderListView

app_name = 'mainapp'

urlpatterns = [
    path('orders/', OrdersView.as_view()),
    path('api/v1/orders/', OrderListView.as_view()),
]
