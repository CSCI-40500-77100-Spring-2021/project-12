from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from SE.models import Assignment, Notes


class CreateUserForm(UserCreationForm):
        class Meta:
                model = User
                fields = ['username','password1','password2']
                
class AssignmentForm(ModelForm):
        class Meta:
                model = Assignment
                fields = '__all__'

class NotesForm(ModelForm):
        class Meta:
                model = Notes
                fields = '__all__'
