from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils.timezone import timezone

class Category(models.Model):
   name = models.CharField(max_length = 30)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('home')  

class Post(models.Model):
   title = models.CharField(max_length = 250)
   header_image = models.ImageField(null=True, blank=True, upload_to="images/")
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   body = models.TextField()
   post_date = models.DateField(auto_now_add=True)
   category = models.CharField(max_length=30, default='sin_categoria')

   def __str__(self):
      return self.title + ' | ' + str(self.author)

   def get_absolute_url(self):
      return reverse('article-detail', args=[(str(self.id))])

class Comment(models.Model):
   post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)      
   name = models.CharField(max_length=250)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return '%s - %s' % (self.post.title, self.name)

   def get_absolute_url(self):
      return reverse('add_comment', args=[(str(self.id))])