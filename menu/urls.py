from django.urls import path
from . import views
from .views import BbCreateView
urlpatterns = [

    path('', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('create/', BbCreateView.as_view(), name='create'),
    path('Quiz/', views.start_the_quiz, name='start_quiz'),
    path('results/', views.results, name='results')
]
