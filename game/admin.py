from django.contrib import admin
from .models import GameProgress, Question, Score
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    list_display = ('question_text', 'option_1', 'correct_answer')
    search_fields = ['question_text']
    summernote_fields = ('question_text',)

# Register your models here.
admin.site.register(GameProgress)
admin.site.register(Score)