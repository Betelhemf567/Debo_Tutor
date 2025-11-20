from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'subject', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resource title (e.g., Chapter 5 Notes)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Brief description of the resource',
                'rows': 3
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.txt,.doc,.docx,.jpg,.jpeg,.png'
            })
        }
        help_texts = {
            'file': 'Allowed formats: PDF, TXT, DOC, DOCX, JPG, PNG (Max 10MB)'
        }
