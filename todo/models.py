#-*- coding: utf-8 -*-

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    statue = models.CharField(max_length=2, default='1')
    pubtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%d %s %s %s' % (self.id, self.name, self.statue, self.pubtime)

    class Meta:
        ordering = ['pubtime', 'statue', 'id']