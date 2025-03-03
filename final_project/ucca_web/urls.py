from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('builder/', views.builder, name='builder'),
    path('support/', views.support, name='support'),
]