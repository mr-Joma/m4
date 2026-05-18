# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

                                    #ДЗ(3-4)
from posts.form import PostForm, CategoryForm, TestForm
                                        # HW5
from posts.models import Post, Category, Tag
from posts.posts import get_posts_filter_by_rate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "base.html")

def post(request):
    posts = get_posts_filter_by_rate(2)
    return render (request, template_name='posts/posts.html', context={"posts": posts})

def get_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, template_name="posts/post.html", context={"post": post})

def get_posts_by_category(request, id):
    posts = Post.objects.filter(category_id=id)
    return render(request, template_name="posts/posts.html", context={"posts": posts})

# ДЗ(2)
def posts(request):
    posts = Post.objects.filter(
        is_published=True,
        rating__gt=5
    )

    return render(request, 'posts/posts.html', {'posts': posts})

@login_required
def create_post(request: HttpRequest):

    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            # HW5
            post = Post.objects.create(
                title=cleaned_data["title"],
                content=cleaned_data["content"],
                rate=cleaned_data["rate"],
                image=cleaned_data["image"],
                category_id=cleaned_data["category"],
                user=request.user,
            )
            
            # HW5
            tags = request.POST.getlist("tags")
            post.tags.set(tags)
            
            return redirect("posts")

        return render(request, "posts/create_post.html", context={"error": form.errors})
    
    form = PostForm()

    categories = Category.objects.all()
    
    # HW5
    tags = Tag.objects.all()

    return render(
        request,
        "posts/create_post.html",                          # HW5
        context={"form": form, "categories": categories, "tags": tags},
    )

#ДЗ(3-4)
def category_create(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("posts")

    else:
        form = CategoryForm()

    return render(
        request,
        "posts/category_create.html",
        {"form": form}
    )
    
# lesson5
def edit_post(request: HttpRequest, pk):
    post = get_object_or_404(Post, id=pk)
    categories = Category.objects.all()
    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            post.title = cleaned_data["title"]
            post.content = cleaned_data["content"]
            post.rate = cleaned_data["rate"]
            if cleaned_data.get("image"):
                post.image = cleaned_data["image"]
            post.category_id = cleaned_data["category"]

            post.save()

            return redirect("post", id=post.pk)
        return render(
            request,
            "posts/edit_post.html",
            context={"post": post, "categories": categories, "errors": form.errors},
        )

    return render(
        request,
        "posts/edit_post.html",
        context={"post": post, "categories": categories},
    )

# lesson5
def delete_post(request: HttpRequest, id):

    if request.method == "GET":
        posts = get_object_or_404(Post, id=id)

        posts.delete()

        return redirect("posts")