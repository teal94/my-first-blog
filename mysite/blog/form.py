from django import forms
from .models import Post
from .models import Category
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'img', 'file',)
        # widgets ={
        #     'title' : forms.TextInput(attrs={'id':'in-title'})
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)