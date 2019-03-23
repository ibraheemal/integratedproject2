# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext

from django.http import HttpResponse
from django.views import View
from .models import QuizObject, Question


# Create your views here.

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

def QuizPage(request,slug):
    context_dict={}
    try:
        quiz_list = QuizObject.objects.get(slug=slug)
        questions = Question.objects.filter(quiz=quiz_list)
        context_dict = {'quizzes': quiz_list.quiz_name, 'qs':questions}
    except QuizObject.DoesNotExist:
        pass
    return render(request,'quiz.html',context_dict)

def QuestionItem(request,slug,pk):
    try:
        context_dict={}
        quizzes = QuizObject.objects.get(slug=slug)
        questions = Question.objects.filter(id=pk)
        context_dict = {'questions': questions, 'quizzes':quizzes}
    except Question.DoesNotExist:
        pass

    return render(request,'question.html',context_dict)
