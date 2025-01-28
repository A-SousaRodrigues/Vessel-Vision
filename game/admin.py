from django.contrib import admin
from .models import GameProgress, Question, Score

# Register your models here.
admin.site.register(GameProgress)
admin.site.register(Question)
admin.site.register(Score)