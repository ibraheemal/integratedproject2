# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class QuizObject(models.Model):
    quiz_name = models.CharField(max_length=50)
    url_slug = models.SlugField()
    def save(self,*args,**kwargs):
        self.url_slug = slugify(self.quiz_name)
        super(QuizObject,self).save(*args,**kwargs)
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(QuizObject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class RegularUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    university = models.CharField(max_length=35)
    def __str__(self):
        return self.user.username
