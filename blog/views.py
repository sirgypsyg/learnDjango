from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [ 
    {
        'author': 'Gypsy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 11, 2031'
    },    
    {
        'author': 'maciek',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'Janurary 44, 1121'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})