from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matchscout/', views.matchscout_view, name='matchscout'),
    path('teamsummary/', views.teamsummary, name='teamsummary'),
]