from django.urls import path

from ep05.drf import views


urlpatterns = [
    path('orders/', views.OrderListCreate.as_view(), name='orders'),
    path('orders/<int:number>', views.OrderRetrieveUpdateDestroy.as_view(), name='order'),
]
