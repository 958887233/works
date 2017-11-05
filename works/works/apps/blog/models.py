# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='covers/%Y/%m/%d')
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('date_created',)

    def __unicode__(self):
        return self.title
