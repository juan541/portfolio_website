from django.shortcuts import render
from .models import Projects
# Create your views here.

def project_list(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def full_view(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'full_view.html', context)