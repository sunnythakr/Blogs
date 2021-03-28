from django.contrib import admin
from django.urls import path
from BlogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list_view),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\{2})/(?P<post>[-\W]+/)', views.post_detail_view, name = 'post_detail'),
    path('(?P<id>\d+)/share/',views.mail_send_view),
    path('tag/(?P<tag_slug>[-\W]+)/', views.post_list_view, name ='post_list_by_tag_name'),
]