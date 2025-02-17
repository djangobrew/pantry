from django.urls import path

from ep05 import drf_views, dj_ninja_views


app_name = 'ep05'

urlpatterns = [
    path('drf/1/', drf_views.drf1, name='drf1'),
    path('ninja/', dj_ninja_views.api.urls, name='ninja'),
]
