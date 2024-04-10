from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' by ' + str(self.author) + '      ' + str(self.date_posted)
    
    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))
        #return reverse('home')