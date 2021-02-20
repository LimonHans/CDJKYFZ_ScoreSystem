from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()

    def __str__(self):
        return self.title

class PostCat(models.Model):
    title = models.CharField(max_length = 200, help_text = "标题")
    content = models.TextField(help_text = "内容")

    def __str__(self):
        return self.title