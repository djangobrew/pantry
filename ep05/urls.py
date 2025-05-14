from django.urls import path, include

from ep05.ninja.views import api as ninja_api
from ep05 import views


app_name = 'ep05'

urlpatterns = [
    path('', views.home, name='home'),
    path('drf-examples/', views.drf_examples, name='drf-examples'),
    path('ninja-examples/', views.ninja_examples, name='ninja-examples'),
    path('vanilla/', include('ep05.vanilla.urls'), name='vanilla'),
    path('drf/', include('ep05.drf.urls'), name='drf'),
    path('ninja/', ninja_api.urls, name='ninja'),
]
