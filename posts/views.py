from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from posts.models import Post, Category, Tag


# ГЛАВНАЯ
class HomeView(TemplateView):
    template_name = "base.html"



# СПИСОК ПОСТОВ
class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):

        return Post.objects.all().order_by("-views", "-created_at")


# ДЕТАЛЬНЫЙ ПОСТ
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):

        post = super().get_object(queryset)
        post.views += 1
        post.save()

        return post


# СОЗДАНИЕ ПОСТА
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "rate", "image", "category"]
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        tags = self.request.POST.getlist("tags")
        self.object.tags.set(tags)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()

        return context


# РЕДАКТИРОВАНИЕ ПОСТА
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "posts/edit_post.html"
    fields = ["title", "content", "rate", "image", "category", "tags"]

    pk_url_kwarg = "id"
    success_url = reverse_lazy("posts")



# УДАЛЕНИЕ ПОСТА
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/delete_post.html"

    pk_url_kwarg = "id"
    success_url = reverse_lazy("posts")



# КАТЕГОРИИ
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "posts/category_create.html"
    fields = ["name"]

    success_url = reverse_lazy("posts")



class PostByCategoryView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):

        category_id = self.kwargs["id"]

        return Post.objects.filter(
            category_id=category_id
        )