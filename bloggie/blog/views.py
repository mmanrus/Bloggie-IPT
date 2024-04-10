from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm
# Create your views here.

#def about(request):
#    return render(request, 'blog/about.html', {'title': 'About Page'})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    fields = ['title', 'title_tag', 'body']
    
# TODO DELETE POST VIEW