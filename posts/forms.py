from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'poster_url',
        ]
        labels = {
            'title': 'Título',
            'content': "Conteúdo",
            'poster_url': 'URL do Poster',
        }