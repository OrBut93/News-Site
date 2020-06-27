from django.forms import ModelForm
from .models import Category, Post


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'views']
