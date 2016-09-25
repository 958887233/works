from django.contrib import admin
from works.apps.blog.models import *

# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)