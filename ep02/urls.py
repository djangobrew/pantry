from django.urls import path

from ep02 import views


app_name = 'ep02'

urlpatterns = [
    path('form1/', views.form1, name='form1'),
    path('modelform1/', views.modelform1, name='modelform1'),
    path('modelform2/', views.modelform2, name='modelform2'),
    path('widgettweaks1/', views.widgettweaks1, name='widgettweaks1'),
    path('crispyforms1/', views.crispyforms1, name='crispyforms1'),
    # path('formset/', views.basic_formset, name='basic_formset'),
    path('success/', views.form_success, name='success'),
]
