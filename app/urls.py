from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('api/get-quiz/', views.get_quiz, name='get-quiz'),
]