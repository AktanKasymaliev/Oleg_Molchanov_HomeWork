from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'blogs/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blogs/post_detail.html', {'post':post})