from django.db import models
from django.forms import forms


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    currentDate = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    viewsCounter = models.IntegerField(default=0)

    def __str__(self):
        return self.title



