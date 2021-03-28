from django.shortcuts import render,get_object_or_404
from BlogApp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

# from taggit.models import Tag

def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    paginator=Paginator(post_list,2) # Paginator how many post you want to show per page  "next & Previous"
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number) 
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'BlogApp/post_list.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)

    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=="POST":
        form =CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()

    # return render (request,'BlogApp/post_detail.html',{'post':post,})
    return render (request,'BlogApp/post_detail.html',{'post':post,"form":form,"csubmit":csubmit,'comments':comments})

from django.core.mail import send_mail
from BlogApp.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail('subject','message','sunnydevnath14@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    form=EmailSendForm()
    return render(request,'BlogApp/sharebyemail.html',{'form':form,'post':post,'sent':sent})



# paginator concept is about how many pages you want to show suppose you have 1000 posts then use paginator "next and Previous "











# #comment
