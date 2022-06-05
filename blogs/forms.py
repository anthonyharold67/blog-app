from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'status','category')
        label = {"image":"Image URL"}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        label = {"body":"Comment"}