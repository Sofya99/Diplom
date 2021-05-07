from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('SearchResult_choice1/', views.SearchResult, name='SearchResult'),
    path('SearchResult_1/', views.SearchResult_1, name='SearchResult_1'),
    path('SearchResult_2/', views.SearchResult_2, name='SearchResult_2'),
    path('SearchResult_3/', views.SearchResult_3, name='SearchResult_3'),
    path('Export/', views.Export, name='Export'),
    path('Ex/', views.Ex, name='Ex'),
    path('Show/', views.Show, name='Show'),
    path('Export_csv_albedo/', views.Export_csv, name='Export_csv'),
    path('Export_csv_sum/', views.Export_csv_sum, name='Export_csv_sum'),
    path('Export_csv_str/', views.Export_csv_str, name='Export_csv_str'),
    path('Export_csv_diff/', views.Export_csv_diff, name='Export_csv_diff'),
    path('Export_csv_sum_1/', views.Export_csv_sum_1, name='Export_csv_sum_1'),
    path('Export_csv_str_1/', views.Export_csv_str_1, name='Export_csv_str_1'),
    path('Export_csv_diff_1/', views.Export_csv_diff_1, name='Export_csv_diff_1'),
    path('Export_csv_sum_2/', views.Export_csv_sum_2, name='Export_csv_sum_2'),
    path('Export_csv_str_2/', views.Export_csv_str_2, name='Export_csv_str_2'),
    path('Export_csv_diff_2/', views.Export_csv_diff_2, name='Export_csv_diff_2'),
    path('Export_csv_sum_3/', views.Export_csv_sum_3, name='Export_csv_sum_3'),
    path('Export_csv_str_3/', views.Export_csv_str_3, name='Export_csv_str_3'),
    path('Export_csv_diff_3/', views.Export_csv_diff_3, name='Export_csv_diff_3'),
    path('FindName/', views.FindName, name='FindName'),
    path('FindNumber/', views.FindNumber, name='FindNumber'),
    path('FindCoord/', views.FindCoord, name='FindCoord'),
    path('ShowStations/', views.ShowStations, name='ShowStations')

]