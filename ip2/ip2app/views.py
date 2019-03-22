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
    try:
        quiz_list = QuizObject.objects.get(slug=slug)
        questions = Question.objects.filter(quiz=quiz_list)
        context_dict = {'quizzes': quiz_list.quiz_name, 'qs':questions}
    except QuizObject.DoesNotExist:
        pass
    return render(request,'quiz.html',context_dict)

#@TODO: fix this so that it shows info. Also, should not be showing
#       anything if i query a url slug that doesn't match to the
#       corresponding URL slug in the models record... idk why this is
#       rendering... probably to do with a doesNotExist exception in
#       views.py
def QuestionItem(request, url_slug):
    context_dict = {}
    try:
        questionQuiz = Question.objects.get(url_slug = url_slug)
        context_dict['questionQuiz'] = questionQuiz

        questionItem = Question.objects.filter(quiz=questionQuiz)
        context_dict['questionItem'] = QuestionItem
    except Question.DoesNotExist or QuizObject.DoesNotExist:
        pass
    return render(request,'quiz.html',context_dict)
