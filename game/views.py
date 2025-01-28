from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import GameProgress, Question
from django.contrib.auth.models import User

# Display the home page
def index(request):
    return render(request,"game/index.html")

# Display the first question or the current question
def game_view(request):
    # Get or create the game progress for the user
    game_progress, created = GameProgress.objects.get_or_create(user=request.user)

    # If the game is completed, redirect to the summary view
    if game_progress.completed:
        return redirect('game_summary')

    # Fetch the current question
    current_question_id = game_progress.current_question
    question = get_object_or_404(Question, id=current_question_id + 1)

    return render(request, 'game/game_view.html', {
        'question': question,
        'game_progress': game_progress,
    })

# Process the submitted answer
def process_answer(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')

        # Get or create the game progress for the user
        game_progress, created = GameProgress.objects.get_or_create(user=request.user)

        # Fetch the current question
        current_question_id = game_progress.current_question
        question = get_object_or_404(Question, id=current_question_id + 1)

        # Check if the user's answer is correct
        if user_answer and user_answer.lower().strip() == question.correct_answer.lower().strip():
            game_progress.score += 1

        # Update progress
        game_progress.current_question += 1

        # Check if the game is complete
        if game_progress.current_question >= Question.objects.count():
            game_progress.completed = True
        game_progress.save()

        # Redirect to the next question or summary
        if not game_progress.completed:
            return redirect('game_view')
        else:
            return redirect('game_summary')

    return redirect('game_view')

# Display the game summary
def game_summary(request):
    # Get the user's game progress
    game_progress = get_object_or_404(GameProgress, user=request.user)

    return render(request, 'game_summary.html', {
        'game_progress': game_progress,
    })

# Reset the game
def reset_game(request):
    game_progress = get_object_or_404(GameProgress, user=request.user)
    game_progress.current_question = 0
    game_progress.score = 0
    game_progress.progress_percentage = 0.0
    game_progress.completed = False
    game_progress.save()
    return redirect('game_view')
