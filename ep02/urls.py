from django.urls import path

from ep02 import views


app_name = 'ep02'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('form1/', views.form1, name='form1'),
    path('modelform1/', views.modelform1, name='modelform1'),
    path('modelform2/', views.modelform2, name='modelform2'),
    path('widgettweaks1/', views.widgettweaks1, name='widgettweaks1'),
    path('crispyforms1/', views.crispyforms1, name='crispyforms1'),
    path('success/', views.form_success, name='success'),
    path('htmx1/', views.htmx1, name='htmx1'),
    path('htmx1-post/', views.htmx1_post, name='htmx1-post'),
    path('htmx2/', views.htmx2, name='htmx2'),
    path('htmx2-post/', views.htmx2_post, name='htmx2-post'),
]
