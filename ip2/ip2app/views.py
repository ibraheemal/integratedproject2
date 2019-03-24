# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from .models import QuizObject, Question
from .forms import QuestionForm


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

class QuestionItem(TemplateView):
    def get(self,request,slug,pk,*args,**kwargs):

        try:
            form = QuestionForm()
            template_name = "question.html"
            quizzes = QuizObject.objects.get(slug=slug)
            questions = Question.objects.filter(id=pk)

            context_dict = {'form':form,'questions': questions, 'quizzes':quizzes,}

        except Question.DoesNotExist:
            pass
        return render(request,'question.html',context=context_dict)

    def post(self,request,slug,pk,*args,**kwargs):
        form = QuestionForm()
        if form.is_valid():
            form.save(commit=True)
        return render(request,'question.html',)
