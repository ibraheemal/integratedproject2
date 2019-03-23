# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class QuizObject(models.Model):
    quiz_name = models.CharField(max_length=50)
    slug = models.SlugField()
    def save(self,*args,**kwargs):
        self.slug = slugify(self.quiz_name)
        super(QuizObject,self).save(*args,**kwargs)
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(QuizObject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_answer = models.CharField(max_length=200, blank=True)
    def save(self,*args,**kwargs):

        super(Question,self).save(*args,**kwargs)
    def __str__(self):
        return self.question_text

class RegularUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    userName = models.CharField(max_length=18)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    university = models.CharField(max_length=35)
    def __str__(self):
        return self.user.username

class UserQuiz(models.Model):
    #m:n relationship; using intermediary model to represent this (M:1,1:M)
    user = models.ForeignKey(RegularUser,on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizObject,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
