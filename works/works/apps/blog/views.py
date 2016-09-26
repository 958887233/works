from django.shortcuts import render, get_object_or_404
from works.apps.blog.models import Blog, Category


# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-date_created')[:3]
    categorys = Category.objects.all()

    return render(request,'blog/index.html', {'blogs': blogs, 'categorys': categorys})


def full_width(request, category=None):
    if category:
        blogs = Blog.objects.filter(category__name_id=category).order_by('-date_created')
    else:
        blogs = Blog.objects.all().order_by('-date_created')
    return render(request, 'blog/full-width.html', {'blogs': blogs})

def about(request):
    return render(request, 'blog/about.html',{})

def contact(request):
    return render(request, 'blog/contact.html', {})


def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/single.html', {'blog': blog})