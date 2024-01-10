from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/get_quiz/', views.get_quiz, name='get_quiz'),
]
