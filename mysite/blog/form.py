from django import forms
from .models import Post
from .models import Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)