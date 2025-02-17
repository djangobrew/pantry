from django.urls import path

from ep05 import drf_views, dj_ninja_views


app_name = 'ep05'

urlpatterns = [
    path('drf/1/', drf_views.drf1, name='drf1'),
    path('drf/orders/', drf_views.OrderListCreate.as_view(), name='order-list'),
    path('drf/orders/<int:number>', drf_views.OrderRetrieveUpdateDestroy.as_view(), name='order2'),
    path('drf/orders/<int:pk>', drf_views.OrderRetrieveUpdateDestroy.as_view(), name='order'),
    path('ninja/', dj_ninja_views.api.urls, name='ninja'),
]
