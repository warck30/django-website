# main/views.py
from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'main/home.html')

def education_skills(request):
    return render(request, 'main/education_skills.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def contacts(request):
    return render(request, 'main/contacts.html')
