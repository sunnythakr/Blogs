from BlogApp.models import Post
from django import template
register =template.Library()


# @register.simple_tag() 
@register.simple_tag(name="my_tag")  # the usage of simple_tag to return number of post published 
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('BlogApp/latest_posts123.html')  # usage of inclusion_tag to dispaly Latest Posts 
def show_latest_posts(count=3): # you can write how many post you want 
    latest_posts =Post.objects.order_by('-publish')[:count]  # Most recent Three [:3] or [:count] whtaever post you want to show 
    return {'latest_posts':latest_posts}
  


from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]   # ('-total_commments')"-" minus here top most comment then after that and then 



    






# post.objects.annotete(total_comments=Count('comments')).order_by('total_comments')



# usase of "assignment_tag" to display the most commented Posts 
# usage of "inclusion_tag"  to dispaly Latest Posts 