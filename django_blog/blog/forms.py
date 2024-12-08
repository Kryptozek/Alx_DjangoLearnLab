from django import forms
from .models import Post
from .models import Comment
from .models import Tag
from taggit.forms import TagWidget 

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget for the tags field
        required=False
    )
    class Meta:
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content',
        }
        
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
