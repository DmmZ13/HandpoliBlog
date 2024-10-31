from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .temp_data import post_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:list')  # Ajuste a URL de sucesso conforme necessário

    def get_success_url(self):
        return reverse_lazy('posts:detail', args=[self.object.id])
    
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    
    def get_success_url(self):
        return reverse_lazy('posts:detail', args=[self.object.id])

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')
