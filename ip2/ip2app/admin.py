# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import QuizObject,Question,RegularUser,UserQuiz

class QuizObjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('quiz_name',)}
admin.site.register(QuizObject,QuizObjectAdmin)
admin.site.register(UserQuiz)
admin.site.register(Question)
admin.site.register(RegularUser)

# Register your models here.
