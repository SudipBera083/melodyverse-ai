from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('generator/', views.lyrics_generator, name='lyrics_generator'),
]