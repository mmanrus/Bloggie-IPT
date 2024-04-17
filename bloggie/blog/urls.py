from django.urls import path
#from . import views
from .views import *



urlpatterns = [
    #path('', views.Home, name="blog-home"),
    #path('about/', views.about, name='about')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('addpost/', AddPost.as_view(), name='add-post'),
    path('addcategory/', AddCategory.as_view(), name='add-category'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/update/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:categories>/', CategoryView, name = 'category'),
    path('category-list/', CategoryListView, name = 'category-list'),
]
