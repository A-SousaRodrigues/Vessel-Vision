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


# Question Model
class Question(models.Model):
    """
    A Django model representing a multiple-choice question.
    """
    
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

# Score Model
class Score(models.Model):
    """
    A model representing a user's score in the game related to :model:`auth.User`.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_completed = models.DateTimeField(auto_now_add=True)


from django.db import models


class Testimonial(models.Model):
    """
    A model to store testimonials for the website.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the user providing the testimonial.")
    testimonial_text = models.TextField(help_text="The testimonial content.")
    date_submitted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, help_text="Only approved testimonials are shown.")

    def __str__(self):
        return self.testimonial_text[:50]  # Show first 50 characters in the admin panel

