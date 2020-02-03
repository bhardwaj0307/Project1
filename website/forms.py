from django import forms
from django.forms import ModelForm
from .models import addProject,addtask
class userLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    # firstName=forms.CharField(max_length=100)
    # lastName=forms.CharField(max_length=100)

class addProjectdetail(ModelForm):
    class Meta:
        model=addProject
        fields="__all__"
class addtaskdetail(ModelForm):
    class Meta:
        model=addtask
        fields="__all__"