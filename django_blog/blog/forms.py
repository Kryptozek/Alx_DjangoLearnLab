from django import forms
from .models import Post
from .models import Comment
from .models import Tag
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
    tags = TagField(required=False)
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
