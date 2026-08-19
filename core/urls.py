from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('track-click/<int:project_id>/', views.track_project_click, name='track_project_click'),
]