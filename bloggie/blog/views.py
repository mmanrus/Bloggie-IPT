from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

#def about(request):
#    return render(request, 'blog/about.html', {'title': 'About Page'})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')
    
class AddCategory(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'blog/add_category.html'
    fields = '__all__'
    
def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'blog/categories.html', {'category': categories.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'category_menu_list': cat_menu_list })

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields = ['title', 'title_tag', 'body']
    
# TODO DELETE POST VIEW
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy("home")
    