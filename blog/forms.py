from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'preview', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'preview': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }