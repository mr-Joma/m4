from django.db import models
from django.contrib.auth.models import User

# CERATE TABLE IF NOT EXISTS ...
# class Model(models.Model): ...

# SELECT * FROM posts
# modelname.objects.all()

# SELECT * FROM posts WHERE ...
# modelname.objects.filter()

# UPDATE model SET id = 2 ...
# modelname.title = 12300
# modelname.save()

# Пример: (Эти 3 сточки замееняювь большой SQL запрос)
# post = Post.objects.get(id=1)
# post.title = "new title"
# post.save() 

# Удаление
# model.name.objects.get(id=1)
# modelname.delete()
# modelname.save()


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False) # ДЗ(2)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    
    tags = models.ManyToManyField(Tag, blank=True) # HW5 / убрал null=True
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.title}  - -  {self.content[:10]}"
    
    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Post"
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        
    def __str__(self):
        return f"{self.name}"
    