from django.urls import path, include
from . import views

urlpatterns = [
    path('initialize/', views.initialize, name='initialize'),
    path('get-cars/', views.get_cars, name='get-cars'),
]
