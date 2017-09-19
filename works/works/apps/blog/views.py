from django.shortcuts import render, get_object_or_404
from works.apps.blog.models import Blog, Category
from works.apps.blog.forms import BlogForm


# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-date_created')[:6]
    categorys = Category.objects.all()
    blogs = [blogs[i:i+2] for i in range(2)]

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

def category(request, category):
    blogs = Blog.objects.filter(category__name=category)
    return render(request, 'blog/category.html', {'blogs': blogs})


def blog_form(request):
    blog_form = BlogForm()

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)

    return render(request, 'blog/edit.html', {'form': blog_form})