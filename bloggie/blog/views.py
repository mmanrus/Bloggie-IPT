from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

#def about(request):
#    return render(request, 'blog/about.html', {'title': 'About Page'})


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        
        cat_menu = Category.objects.all()
        context["cat_menu"] = cat_menu
        """
        stuff = get_object_or_404(Post, id="self".kwargs['pk'])
        total_likes = stuff.total_likes()
        
        context["total_likes"] = total_likes
        return context
        """
        pk = self.kwargs.get('pk')  # Corrected the retrieval of pk
        
        total_likes = 0
        if pk:
            post = get_object_or_404(Post, pk=pk)
            total_likes = post.total_likes()

        context["total_likes"] = total_likes
        
        return context
class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        # Retrieve a single post and its total likes
        pk = self.kwargs.get('pk')  # Corrected the retrieval of pk
        total_likes = 0
        liked = False
        if pk:
            post = get_object_or_404(Post, pk=pk)
            total_likes = post.total_likes()

            # Check if the post exists and if the current user has liked it
            if post and post.likes.filter(id=self.request.user.id).exists():
                liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        
        return context
    
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
"""
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'category_menu_list': cat_menu_list })
"""

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'category_menu_list': category_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
       post.likes.add(request.user)
       liked = True
    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy("home")
    