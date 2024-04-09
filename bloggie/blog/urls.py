from django.urls import path
#from . import views
from .views import *



urlpatterns = [
    #path('', views.Home, name="blog-home"),
    #path('about/', views.about, name='about')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
]
