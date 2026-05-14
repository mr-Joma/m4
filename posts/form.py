from django.forms import ModelForm, Form, CharField, IntegerField, ImageField

                              # ДЗ(3-4)  # HW5
from posts.models import Post, Category, Tag


class PostForm(ModelForm):
    class Meta:
        model = Post                                                
        fields = ["title", "content", "rate", "category", "image"]
        
 # ДЗ(3-4)       
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        
# lesson 5
class TestForm(Form):
    title = CharField(max_length=255, required=False)
    content = CharField(required=False)
    rate = IntegerField(min_value=1, max_value=10, required=False)
    category = IntegerField(required=False)
    image = ImageField(required=False)
    tags = CharField(required=False) # HW5