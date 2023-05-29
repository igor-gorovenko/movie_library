from django import forms

from .models import Reviews


class ReviewForms(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        
