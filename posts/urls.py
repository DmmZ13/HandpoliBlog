from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='index'), # adicione esta linha
    path('<int:post_id>/', views.detail_post, name='detail'), # adicione esta linha
    path('create/', views.create_post, name='create'), # adicione esta linha
]