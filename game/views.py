from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameProgress, Question, Score
from django.http import JsonResponse

# Game Views

@login_required
def game_view(request):
    """
    Displays the current question and tracks the user's progress.
    """
    # Get the user's current game progress
    game_progress, created = GameProgress.objects.get_or_create(user=request.user)
    
    # Get the current question based on the user's progress
    current_question = game_progress.current_question
    question = Question.objects.all()[current_question] if current_question < Question.objects.count() else None
    
    if not question:
        return redirect('game_summary')
    
    return render(request, 'game/game_view.html', {'question': question})

@login_required
def process_answer(request):
    game_progress = GameProgress.objects.get(user=request.user)

    # Get the current question
    question = Question.objects.get(id=game_progress.current_question)

    # Check if the answer is correct
    user_answer = request.POST.get('answer')
    if user_answer == question.correct_answer:
        game_progress.score += 1

    # Update the user's progress
    game_progress.current_question += 1
    game_progress.save()

    # Prepare the response: Either show the next question or end the game
    if game_progress.current_question < Question.objects.count():
        next_question = Question.objects.all()[game_progress.current_question]
        return JsonResponse({'next_question': next_question.question_text})
    else:
        return JsonResponse({'next_question': None})

@login_required
def game_summary(request):
    """
    Displays a summary of the user's performance in the game.
    """
    game_progress = GameProgress.objects.get(user=request.user)
    
    # Save score and summary after game completion
    Score.objects.create(user=request.user, score=game_progress.score)
    
    return render(request, 'game/game_summary.html', {
        'score': game_progress.score,
        'progress_percentage': game_progress.progress_percentage
    })



