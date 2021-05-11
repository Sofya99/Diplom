from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('SearchResult/', views.SearchResult, name='SearchResult'),
    path('Export/', views.Export, name='Export'),
    path('Ex/', views.Ex, name='Ex'),
    path('Show/', views.Show, name='Show'),
    path('Export_csv/', views.Export_csv, name='Export_csv'),
    path('FindName/', views.FindName, name='FindName'),
    path('FindNumber/', views.FindNumber, name='FindNumber'),
    path('FindCoord/', views.FindCoord, name='FindCoord'),
    path('ShowStations/', views.ShowStations, name='ShowStations')

]