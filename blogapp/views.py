from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'blogapp/index.html',{
        'posts':posts
    })

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'blogapp/post_detail.html',{
        'post':post
    })
