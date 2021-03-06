#coding=utf-8
import json
from django.shortcuts import render, get_object_or_404
from works.apps.blog.models import Blog, Category
from works.apps.blog.forms import BlogForm
from django.http import JsonResponse, HttpResponse


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]


def index(request):
    blogs = Blog.objects.all().order_by('-date_created')[:4]
    categorys = Category.objects.all()
    display_blogs = chunks(blogs, 2)

    return render(
        request,
        'blog/index.html',
        {'blogs': blogs, 'display_blogs': display_blogs, 'categorys': categorys}
    )


def full_width(request, category=None):
    if category:
        blogs = Blog.objects.filter(category__name_id=category) \
                .order_by('-date_created')
    else:
        blogs = Blog.objects.all().order_by('-date_created')
    return render(request, 'blog/full-width.html', {'blogs': blogs})


def about(request):
    return render(request, 'blog/about.html',{})


def contact(request):
    return render(request, 'blog/contact.html', {})


def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blog': blog})


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def category(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/category.html', {'blogs': blogs})


def blog_form(request):
    categorys = Category.objects.all()
    blog_form = BlogForm()

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)

    return render(
        request,
        'blog/edit.html',
        {'form': blog_form, 'categorys': categorys}
    )
