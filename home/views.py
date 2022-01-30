from django.shortcuts import render, HttpResponse
from .models import Project,Skills

# Create your views here.

def index(request):

    projects=Project.objects.all()
    skills=Skills.objects.all()
    
    context={
        '':index,
        'projects':projects,
        'skills':skills

    }
    return render(request, 'index.html', context)
    



