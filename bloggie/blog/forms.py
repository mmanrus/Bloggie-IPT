from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'author': forms.Select(attrs={'class': 'form-control border border-dark-subtle'}),
            'category': forms.Select(attrs={'class': 'form-control border border-dark-subtle'}),
            'body': forms.Textarea(attrs={'class': 'form-control border border-dark-subtle'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            #'author': forms.Select(attrs={'class': 'form-control border border-dark-subtle'}),
            'body': forms.Textarea(attrs={'class': 'form-control border border-dark-subtle'}),
        }