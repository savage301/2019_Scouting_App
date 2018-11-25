from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matchscout/', views.matchscout, name='matchscout'),
]