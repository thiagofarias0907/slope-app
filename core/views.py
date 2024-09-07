from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.db.models import Q

Project = apps.get_model('project_management', 'Project')
Methodology = apps.get_model('project_management', 'MethodologySteps')
Steps = apps.get_model('project_management', 'Steps')
ProjectHistory = apps.get_model('project_management', 'ProjectHistory')
Users = apps.get_model('accounts','UserProfile')
Person = apps.get_model('project_management', 'Person')

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    template = 'base.html'

    active_projects = Project.objects.filter(Q(status=1)|Q(status=2))
    inactive_projects = Project.objects.filter(status=4)
    done_projects = Project.objects.filter(status=3)
    methodologies = Methodology.objects.all()
    steps = Steps.objects.all()
    users = Users.objects.all()
    team = Person.objects.all()
    context ={
        'active_projects': len(active_projects),
        'inactive_projects': len(inactive_projects),
        'done_projects': len(done_projects),
        'methodologies':len(methodologies),
        'users' : len(users),
        'team' : len(team),
        'steps':steps
    }
    return render(request, template_name=template, context=context)