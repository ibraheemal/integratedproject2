# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext

from django.http import HttpResponse
from django.views import View
from .models import QuizObject, Question


# Create your views here.
from.models import QuizObject,Question
def Index(View):
    info = 'bla bla bla'
    context_dict = {'boldmsg': "i am a bold message"}
    return render_to_response('index.html',context_dict)

def About(View):
    return HttpResponse("about page")

def SignInRegister(View):
    return HttpResponse("sign in or register ")

def Profile(View):
    return HttpResponse("profile")

def ScoreBoard(View):
    return HttpResponse("example scoreboard")

def Quiz(request):
    quiz_list = QuizObject.objects.order_by('quiz_name')
    context_dict = {'quizzes': quiz_list}
    return render(request,'quiz.html',context_dict)
