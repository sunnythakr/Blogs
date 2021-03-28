from BlogApp.models import Post
from django import template
register =template.Library()

@register.simple_tag

def total_posts():
    return Post.objects.count()