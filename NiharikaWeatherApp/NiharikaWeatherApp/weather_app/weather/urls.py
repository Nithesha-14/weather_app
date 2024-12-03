from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-weather/', views.view_weather, name='view_weather'),
    path('fetch-weather-data/', views.fetch_weather_data, name='fetch_weather_data'),
    path('compare-weather/', views.compare_weather, name='compare_weather'),
    path('search-weather/', views.search_weather, name='search_weather'),
]
