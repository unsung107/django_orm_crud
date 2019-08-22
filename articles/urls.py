from django.urls import path
from . import views

# articles/____
urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),    
]