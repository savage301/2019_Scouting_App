from django.urls import path

from . import views

urlpatterns = [
    path('pitscout/', views.pitscoutview, name='pitscout'),
    path('pitscoutedit/', views.pitscoutedit, name='pitscoutedit'),
]