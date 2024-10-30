from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} ({self.date})'