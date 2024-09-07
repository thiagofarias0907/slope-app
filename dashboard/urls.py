from django.urls import path, include

app_name = 'dashboard'

from . import views


urlpatterns = [
    # path('dashboard/', views.home, name='dashboard'),
    path('dashboard/pie_chart', views.pie_chart, name='pie-chart'),
    path('dashboard/', views.dashboard, name='dashboard'),
]