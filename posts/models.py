from django.db import models

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


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    user = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    udated_at = models.DateTimeField(auto_now=True)
    
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
    