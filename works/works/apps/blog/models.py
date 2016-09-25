# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('date_created',)

    def __unicode__(self):
        return self.title
