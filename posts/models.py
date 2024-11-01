from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} ({self.date})'
    
class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'