from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'school', 'grade_level', 'favorite_subjects']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your school or university'
            }),
            'grade_level': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Grade 10, Year 2 University'
            }),
            'favorite_subjects': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Math, Physics, Chemistry'
            }),
        }
