from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    # Every question might have multiple choices
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
