from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from ep05.drf import views


spectacular_urls = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='ep05:schema'), name='drf-swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='ep05:schema'), name='redoc'),
]

urlpatterns = spectacular_urls + [
    path('orders/', views.OrderListCreate.as_view(), name='orders'),
    path('orders/<int:number>', views.OrderRetrieveUpdateDestroy.as_view(), name='order'),
    path('baristas/', views.BaristaListCreate.as_view(), name='baristas'),
    path('baristas/<int:pk>', views.BaristaRetrieveUpdateDestroy.as_view(), name='barista'),
    path('items/<int:pk>', views.ItemRetrieveUpdateDestroy.as_view(), name='item'),
    path('items/', views.ItemListCreate.as_view(), name='items'),
]
