from posts.models import Post

def get_posts_filter_by_rate(rate):
    
    posts = Post.objects.filter(rate__gt=rate)
    
    return posts

def get_all_posts():
    posts = Post.objects.filter(is_published=True, rating__gt=5) # Изменил
    
    return posts