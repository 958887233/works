from django import forms
from pagedown.widgets import AdminPagedownWidget
from works.apps.blog.models import Blog


class BlogForm(forms.ModelForm):
  content = forms.CharField(widget=AdminPagedownWidget())
  class Meta:
    model = Blog
    fields = '__all__'
