# main/views.py
from django.shortcuts import render
from .models import Project
#Lab2 cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache

@cache_page(60 * 15)
def home(request):
    return render(request, 'main/home.html')

def education_skills(request):
    return render(request, 'main/education_skills.html')

def projects(request):
    projects = cache.get('all_projects')
    if not projects:
        projects = Project.objects.all()
        cache.set('all_projects', projects, 60 * 15)  # 15 mins cache
    return render(request, 'main/projects.html', {'projects': projects})

def contacts(request):
    return render(request, 'main/contacts.html')
