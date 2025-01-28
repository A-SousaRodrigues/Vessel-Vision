from django.contrib import admin
from .models import GameProgress, Question, Score, Testimonial
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    list_display = ('question_text', 'option_1', 'correct_answer')
    search_fields = ['question_text']
    summernote_fields = ('question_text',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('testimonial_text', 'name', 'date_submitted', 'approved')
    list_filter = ('approved', 'date_submitted')
    search_fields = ('testimonial_text', 'name')
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} testimonials approved.")
    approve_testimonials.short_description = "Approve selected testimonials"


# Register your models here.
admin.site.register(GameProgress)
admin.site.register(Score)