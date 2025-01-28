from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('game_view', views.game_view, name='game_view'),
    path('process_answer/', views.process_answer, name='process_answer'),
    path('game_summary/', views.game_summary, name='game_summary'),
    path('reset_game/', views.reset_game, name='reset_game'),
    
]