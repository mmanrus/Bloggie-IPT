from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

#def about(request):
#    return render(request, 'blog/about.html', {'title': 'About Page'})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    
#class AddPost():
#    model