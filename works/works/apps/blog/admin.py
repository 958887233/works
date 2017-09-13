from django.contrib import admin
from works.apps.blog.models import *
from django import forms
from pagedown.widgets import AdminPagedownWidget

# Register your models here.
class BlogForm(forms.ModelForm):
  content = forms.CharField(widget=AdminPagedownWidget())
  class Meta:
    model = Blog
    fields = '__all__'

# class BlogAdmin(admin.ModelAdmin):
#   form = BlogForm


admin.site.register(Category)
admin.site.register(Blog)
