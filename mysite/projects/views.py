from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects': projects})

def about(request):
    return render(request, 'projects/about.html')

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project':project_detail})

def work(request):
    projects = Project.objects
    return render(request, 'projects/work.html', {'projects': projects})