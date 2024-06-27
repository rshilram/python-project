# profiles/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import ProfileForm, ProjectForm


def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_view')
    else:
        profile_form = ProfileForm(instance=profile)
    projects = Project.objects.filter(profile=profile)
    return render(request, 'register.html', {'profile_form': profile_form, 'projects': projects})


def add_project(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.profile = profile
            project.save()
            return redirect('profile_view')
    else:
        project_form = ProjectForm()
    return render(request, 'list.html', {'project_form': project_form})
