from django.forms import ModelForm
                              # ДЗ(3-4)
from posts.models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post                                                
        fields = ["title", "content", "rate", "category", "image"]
        
 # ДЗ(3-4)       
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]