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
def pie_chart(request):
    labels = []
    data = []


    # projects = Project.objects.all()
    # for project in projects:
    #     labels.append(project.name)
    #     data.append(project.id)

    methodologies = Methodology.objects.all()
    projects = Project.objects.all()
    for methodology in methodologies:
        count = 0
        for project in projects:
            if project.methodology.id == methodology.id:
                count = count + 1    
        labels.append(methodology.name)
        data.append(count)

    return render(request, 'dashboard/chart.html', {
        'labels': labels,
        'data': data,
    })

@login_required(login_url='/accounts/login/')
def dashboard(request):

    methodology_pie_chart_data = {
        'data': [],
        'labels': [],
    }
    steps_bar_chart_data = {
        'data': [],
        'labels': [],
    }
    status_bar_chart_data = {
        'data': [],
        'labels': [],
    }
    projecthistory_timeline_chart_data = {
        'data': [],
        'labels': []
    }

    selected_methodology = 0 
    if request.GET.get('methodology') != '' and request.GET.get('methodology') is not None:
        selected_methodology = int(request.GET.get('methodology'))

    methodologies = Methodology.objects.all()
    projects = Project.objects.all()
    for methodology in methodologies:
        count = 0
        for project in projects:
            if project.methodology.id == methodology.id:
                count = count + 1    
        methodology_pie_chart_data.get('labels').append(methodology.name)
        methodology_pie_chart_data.get('data').append(count)

    projects = Project.objects.all()
    steps = Steps.objects.all()
    for step in steps:
        if step.methodology_id != selected_methodology  and selected_methodology > 0:
            continue
        count = 0
        for project in projects:
            if project.step.id == step.id:
                count = count + 1
        steps_bar_chart_data.get('data').append(count)
        steps_bar_chart_data.get('labels').append(step.name)

    
    status_choices = Project.STATUS_CHOICES
    for status in status_choices:
        count = 0
        for project in projects:
            if project.status == status[0]:
                count = count + 1
        status_bar_chart_data.get('data').append(count)
        status_bar_chart_data.get('labels').append(status[1])

    # colors= ['#FFF07C', '#80FF72', '#7EE8FA', '#EEC0C6', '#E58C8A']
    # projects_history = ProjectHistory.objects.filter().order_by('id')
    # labels = [] 
    # for project_history in projects_history:
    #     if project_history.date not in labels:
    #         labels.append(project_history.date)

    # i = 0
    # for project in projects:
    #     data = []
    #     dataset = []
    #     print(project.id)
    #     last_step = 0
    #     for project_history in projects_history:
    #         if project.id == project_history.project_id:
    #             last_step = project_history.step_id
    #             data.append(project_history.step_id)
    #         else:
    #             data.append(last_step)
    #     dataset = {'data':data,'labels':labels, 'color': colors[int((i)%len(colors))], 'name':project.name}
    #     projecthistory_timeline_chart_data.get('data').append(dataset)
    #     i = i + 1        

    colors= ['#FFF07C', '#80FF72', '#7EE8FA', '#EEC0C6', '#E58C8A']
    projects_history = ProjectHistory.objects.filter().order_by('id')
    i = 0
    
    from datetime import date, timedelta
    today = date.today() 
    labels=[]
    for i in range(1,32):
       date_iter = today - timedelta(30-i)
       labels.append(date_iter)     
       projecthistory_timeline_chart_data.get('labels').append(date_iter)
    
    projects_counter = 0
    for project in projects:
        if project.methodology_id != selected_methodology and selected_methodology > 0:
            continue
        projects_counter =  projects_counter +1
        data = []
        dataset = []
        last_step_order = 0
        projects_history = ProjectHistory.objects.filter(project_id=project.id)
        last_date = today - timedelta(31)
        for project_history in projects_history:
            for label in labels:
                if label == project_history.date:
                    last_date = label
                    for step in steps:
                        if step.id == project_history.step_id:
                            last_step_order = step.order
                            data.append(last_step_order)
                elif (label < project_history.date) and (label > last_date):
                    data.append(last_step_order)
                    last_date = label
                
        if len(data) == 0:
            data = [0 for i in range(0,31)]
        dataset = {'data':data, 'color': colors[int((i)%len(colors))], 'name':project.name}
        projecthistory_timeline_chart_data.get('data').append(dataset)
        i = i + 1  

    if selected_methodology > 0:
        active_projects = Project.objects.filter(Q(status=1)|Q(status=2),Q(methodology_id=selected_methodology))
        inactive_projects = Project.objects.filter(Q(status=4),Q(methodology_id=selected_methodology))
        done_projects = Project.objects.filter(Q(status=3),Q(methodology_id=selected_methodology))
    
    if selected_methodology == 0 or selected_methodology is None:
        active_projects = Project.objects.filter(Q(status=1)|Q(status=2))
        inactive_projects = Project.objects.filter(Q(status=4))
        done_projects = Project.objects.filter(Q(status=3))

    steps = Steps.objects.all()
    users = Users.objects.all()
    team = Person.objects.all()


    return render(request, 'dashboard/dashboard.html', {
        'steps_bar_chart_data': steps_bar_chart_data,
        'status_bar_chart_data': status_bar_chart_data,
        'methodology_pie_chart_data': methodology_pie_chart_data,
        'projecthistory_timeline_chart_data': projecthistory_timeline_chart_data,
        'methodologies': methodologies,
        'selected_methodology':selected_methodology,
        'projects_qty': (len(active_projects) + len(inactive_projects) + len(done_projects)),
        'active_projects': len(active_projects),
        'inactive_projects': len(inactive_projects),
        'done_projects': len(done_projects),
        'users' : len(users),
        'team' : len(team),
        'steps':steps
    })

@login_required(login_url='/accounts/login/')
def home(request):
    template = 'dashboard/dashboard.html'

    projects = Project.objects.all()
    context ={
        'projects': projects
    }
    return render(request, template_name=template, context=context)

