from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse('home')
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    body = models.TextField()
    category = models.CharField(max_length=255, default='default category')
    
    def __str__(self):
        return self.title + ' by ' + str(self.author) + ' Date Published: ' + str(self.date_posted)
    
    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))
        #return reverse('home')