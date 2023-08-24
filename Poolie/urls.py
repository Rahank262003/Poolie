from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('driver/', views.driver),
    path('passenger/', views.passenger),
    path('search-ride/', views.search_ride, name='search_ride'),
    path('registration/', views.registration, name='registration'),
]
