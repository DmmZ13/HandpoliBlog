from django.forms import ModelForm
from .models import Post, Comments


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

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }