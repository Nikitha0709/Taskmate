from django import forms
from todo_app.models import TaskList

class Taskform(forms.ModelForm):
     class Meta:
         model = TaskList
         fields=['task','done']
         