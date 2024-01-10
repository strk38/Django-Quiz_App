from django.contrib import admin
from .models import BaseModel, Category, Question, Answer



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

class AnswerAdmin(admin.StackedInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'marks', 'created_at', 'updated_at')
    inlines = [AnswerAdmin]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_correct', 'created_at', 'updated_at')
