from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    n = ['Aktan', 'beka', 'altai']
    context ={
        'name': n
    }
    return render(request, 'blogs/index.html', context)