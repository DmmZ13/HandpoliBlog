from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .temp_data import post_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comments, Category
from .forms import PostForm, CommentsForm
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

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comments(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentsForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'posts/category.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'posts/index.html'  # Reutilizando o template de listagem de posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.object.posts.all()  # Acessa os posts relacionados à categoria
        context['category_name'] = self.object.name  # Passa o nome da categoria
        return context