from django import forms
from .models import Post, Category

#choices = [('entertainment','entertainment'), ('sports', 'sports')....... and all other categories]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
    
print(choice_list)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'author': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle', 'value': '', 'id': 'post_owner', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control border border-dark-subtle'}),
            'body': forms.Textarea(attrs={'class': 'form-control border border-dark-subtle'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border border-dark-subtle'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control border border-dark-subtle'}),
            #'author': forms.Select(attrs={'class': 'form-control border border-dark-subtle'}),
            'body': forms.Textarea(attrs={'class': 'form-control border border-dark-subtle'}),
        }