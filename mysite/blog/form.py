from django import forms
from .models import Post
from .models import Category
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'img', 'file',)

    def __init__(self, *args, **kargs):
        super(PostForm, self).__init__(*args, **kargs)
        self.fields['title'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'제목'})
        self.fields['text'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'내용',
            'rows' : "3"})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
    def __init__(self, *args, **kargs):
        super(CommentForm, self).__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'댓글 작성자'})
        self.fields['text'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'댓글 내용',
            'rows' : "3"})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
    def __init__(self, *args, **kargs):
        super(CategoryForm, self).__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'카테고리 제목 입력'})

