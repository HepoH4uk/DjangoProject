from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Список статей с фильтрацией опубликованных
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        # фильтрация только опубликованных статей
        return super().get_queryset().filter(published=True)

# Детальный просмотр статьи с увеличением счетчика просмотров
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # увеличиваем счетчик просмотров при каждом просмотре
        obj.views_counter += 1
        obj.save(update_fields=['views_counter'])
        return obj

# Создание новой статьи
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

# Обновление статьи с перенаправлением на страницу просмотра после успешного редактирования
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


# Удаление статьи (опционально)
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_del_conf.html'
    success_url = reverse_lazy('blog:post_list')