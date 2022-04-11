from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']
        labels = {
            'title': 'Tytuł',
            'content': 'Treść'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Treść'
        }
