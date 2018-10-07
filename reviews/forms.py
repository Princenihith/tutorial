from django.forms import ModelForm, Textarea
from reviews.models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment',]
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }