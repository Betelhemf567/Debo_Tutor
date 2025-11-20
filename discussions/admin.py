from django.contrib import admin
from .models import Question, Reply

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'subject', 'created_at']
    list_filter = ['subject', 'created_at']
    search_fields = ['title', 'description']

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['question', 'author', 'created_at']
    list_filter = ['created_at']
