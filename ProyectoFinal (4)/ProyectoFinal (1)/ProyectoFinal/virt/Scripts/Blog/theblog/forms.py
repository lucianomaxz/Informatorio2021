from django import forms
from .models import Post, Category
from django.db import models

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
      class Meta:
      	model = Post
      	fields = ('title', 'author', 'category', 'body', 'header_image')

      	widgets = {
      	  'title': forms.TextInput(attrs={'class': 'form-control'}),
      	  'author': forms.Select(attrs={'class': 'form-control'}),
      	  'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
      	  'body': forms.Textarea(attrs={'class': 'form-control'}),
      	}
		