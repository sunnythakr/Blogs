from django.contrib import admin
from BlogApp.models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status',]
    prepopulated_fields ={'slug':('title',)}
    list_filter=('status','author','publish')  #  it is used to show in database like post status (draft or published ), author name(), post date like(last 7 days ,last momth , year like this )
    search_fields=('title','body',)   
    raw_id_fields=('author',) # consider if you have 100 author how would you be do that, it helps you the search fields of author name 
    date_hierarchy='publish'   # it will show you a navbar in the topleft which shows date
    ordering=['status','publish']  # at the top it will be show you created date publish date updated date


admin.site.register(Post,PostAdmin)



# comment section 
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Comment,CommentAdmin)
