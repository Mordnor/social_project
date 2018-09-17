# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    cover = models.ImageField(upload_to="articles")
    friends = models.ManyToManyField('Profile', blank=True)

    def __unicode__(self):
        return self.user.username