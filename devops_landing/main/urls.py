# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education-skills/', views.education_skills, name='education_skills'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
]