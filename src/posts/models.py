from django.db import models
from __future__ import unicode_literals
# Create your models here.

class Post(models.Model):
    title = models.CharField()
    Comment = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=Falsem auto_now_add=True)

    def __unicode__(self):
        return self.title