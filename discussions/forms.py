from django import forms
from .models import Question, Reply

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'subject']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your question title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your question in detail',
                'rows': 5
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your reply here...',
                'rows': 3
            })
        }
        labels = {
            'content': 'Your Reply'
        }
