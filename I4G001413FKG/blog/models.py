from typing import Text
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.Title
