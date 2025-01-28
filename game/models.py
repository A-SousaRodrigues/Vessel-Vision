from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# GameProgress Model
class GameProgress(models.Model):
    """
    Stores the game progress related to :model:`auth.User`.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_question = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    completed = models.BooleanField(default=False)

