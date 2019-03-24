# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RegularUser,Question
from django.forms import ModelForm

# user authentication
#class CustomUserCreationForm(UserCreationForm):

#    class Meta(UserCreationForm):
#        model = RegularUser
#        fields = ('username', 'email')

#class CustomUserChangeForm(UserChangeForm):

#    class Meta:
#        model = RegularUser
#        fields = ('username', 'email')

# quiz / question forms

class QuestionForm(ModelForm):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    user_response = forms.CharField(max_length=200)
    class Meta:
        model = Question
        fields = ('user_response',)
