from works.apps.blog.models import Blog
from pagedown.widgets import AdminPagedownWidget
from django import forms


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Blog