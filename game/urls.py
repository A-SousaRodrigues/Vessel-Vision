from . import views
from django.urls import path

urlpatterns = [
    path('', views.game_view, name='home'),
    path('game/answer/<int:question_id>/', views.process_answer, name='process_answer'),
    path('game/summary/', views.game_summary, name='game_summary'),
]