from django.shortcuts import render
from works.apps.blog.models import Blog

# Create your views here.

def home(request):
    blog = Blog.objects.first()

    return render(request,'blog/index.html', {'blog': blog})


def full_width(request):
    blogs = Blog.objects.all()[:5]
    return render(request, 'blog/full-width.html', {'blogs': blogs})

def about(request):
    return render(request, 'blog/about.html',{})

def contact(request):
    return render(request, 'blog/contact.html', {})


def single(request):
    return render(request, 'blog/single.html', {})