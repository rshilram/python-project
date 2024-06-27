from django import forms
from .models import Profile, Project


class ProfileForm(forms.ModelForm):


  class Meta:
         model = Profile
         fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']