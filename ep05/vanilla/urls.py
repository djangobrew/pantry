from django.urls import path

from ep05.vanilla import views


urlpatterns = [
    path('orders/', views.orders, name='orders'),
]
