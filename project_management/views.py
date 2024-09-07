from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from .forms import ProjectForm,ProjectEditForm, PersonForm, MethodologyForm,MethodologyStepsForm, ProjectHistoryForm
from datetime import date

from .models import Project, Person, Methodology, Steps,MethodologySteps

#MAIN PAGE OF THE PACKAGE
@login_required(login_url='/accounts/login/')
def show_projects(request):
    template = 'project_management/management.html'
    projects = Project.objects.all()
    order_by_filter="id"
    if request.GET.get('order_by') != ''and request.GET.get('order_by') is not None:
        order_by_filter = request.GET.get('order_by')
    if request.GET.get('name_contains') != ''and request.GET.get('name_contains') is not None:
        projects_name_filter = request.GET.get('name_contains')
        projects = projects.filter(name__icontains=projects_name_filter)
    methodologies = MethodologySteps.objects.order_by('id')
    steps = Steps.objects.order_by('order')        
    context ={
        'projects': projects,
        'steps':steps,
        'methodologies':methodologies,
        'order_by':order_by_filter
    }
    return render(request, template_name=template, context=context)

# PROJECTS' VIEW FUNCTIONS
@login_required(login_url='/accounts/login/')
def add_project(request):
    template = 'project_management/create_project.html'
    context = {}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.date = date.today()
            form_save.last_update = date.today()
            form_save.feedback = 4
            form_save.save()
            messages.success(request,'Projeto adicionado com sucesso!')
    form = ProjectForm()
    context['form'] = form
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def edit_project(request, id_project):
    template = 'project_management/create_project.html'
    context = { 'is_edition' : True }
    project = get_object_or_404(Project, id=id_project)
    if request.method == 'POST':
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.last_update = date.today()
            form_save.save()
            project_history_form = ProjectHistoryForm()
            project_history_form_save = project_history_form.save(commit=False)
            project_history_form_save.step_id = form_save.step_id 
            project_history_form_save.step = form_save.step
            project_history_form_save.project_id = project.id
            project_history_form_save.project = project
            project_history_form_save.date  = date.today()
            project_history_form_save.save() 
            return redirect("project_management:management")
    form = ProjectEditForm(instance=project)
    context['form'] = form
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def delete_project(request, id_project):
    project = get_object_or_404(Project, id=id_project)
    project.delete()
    return redirect("project_management:management")

@login_required(login_url='/accounts/login/')
def show_methodologies_steps(request):
    template = 'project_management/methodologies_steps.html'
    methodologies = MethodologySteps.objects.order_by('id')
    steps = Steps.objects.order_by('order')
    context ={
        'methodologies': methodologies,
        'steps': steps
    }
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def edit_methodologies_and_steps(request, id_methodology):
    template = 'project_management/create_methodologysteps.html'
    context = {}
    methodology = get_object_or_404(MethodologySteps, id=id_methodology)
    methodology_steps_formSet = inlineformset_factory(MethodologySteps, Steps, exclude=(), extra=0, can_delete=True)
    if request.method == "POST":
        methodology_form = MethodologyStepsForm(request.POST, instance=methodology)
        formset = methodology_steps_formSet(request.POST, request.FILES,prefix='stepsformset', instance=methodology)
        if formset.is_valid() and methodology_form.is_valid():
            methodology_form.save()
            formset.save()
            messages.success(request,'Metodologia atualizada com sucesso!')
        else:
            messages.warning(request,'Erro ao salvar! Verifique os dados inseridos')
    else:
        methodology_form = MethodologyStepsForm(instance=methodology)
        formset = methodology_steps_formSet(instance=methodology,prefix='stepsformset')
    context['steps_formset'] = formset
    context['methodology_form'] = methodology_form
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def add_methodologies_and_steps(request):
    template = 'project_management/create_methodologysteps.html'
    context = {}
    methodology_steps_formSet = inlineformset_factory(MethodologySteps, Steps, exclude=(), can_delete=False,  min_num= 3, max_num= 10)
    if request.method == "POST":
        methodology_form = MethodologyStepsForm(request.POST)
        formset = methodology_steps_formSet(request.POST, request.FILES,prefix='stepsformset')
        if formset.is_valid() and methodology_form.is_valid():
            methodology_form.save()
            formset_save = formset.save(commit=False)
            for form in formset_save:
                form.methodology = MethodologySteps.objects.get(name=methodology_form.data.get('name'))
                form.save()
            messages.success(request,'Metodologia adicionada com sucesso!')
        else:
            messages.warning(request,'Erro ao salvar! Verifique os dados inseridos')
    else:
        methodology_form = MethodologyStepsForm()
        formset = methodology_steps_formSet(prefix='stepsformset')
    context['steps_formset'] = formset
    context['methodology_form'] = methodology_form
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def delete_methodology_steps(request, id_methodology):
    methodology = get_object_or_404(MethodologySteps, id=id_methodology)
    methodology.delete()
    return redirect("project_management:all_methodologies")


#Person VIEW FUNCTIONS
@login_required(login_url='/accounts/login/')
def add_person(request):
    template = 'project_management/create_team_member.html'
    context = {}
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Membro da equipe adicionado com sucesso!')
        elif not form.is_valid():
            messages.error(request, 'Erro ao adicionar a pessoa!')
    form = PersonForm()
    context['form'] = form
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def edit_person(request, id_person):
    template = 'project_management/create_team_member.html'
    context = {}
    person = get_object_or_404(Person, id=id_person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("project_management:all_team_members")
        elif not form.is_valid():
            messages.error(request, 'Erro ao editar a Pessoa!')
    form = PersonForm(instance=person)
    context['form'] = form
    return render(request, template_name=template, context=context)


@login_required(login_url='/accounts/login/')
def delete_person(request, id_person):
    person = get_object_or_404(Person, id=id_person)
    person.delete()
    return redirect("project_management:all_team_members")

@login_required(login_url='/accounts/login/')
def show_team_members(request):
    template = 'project_management/team_members.html'
    team_members = Person.objects.all()
    context ={
        'team_members': team_members
    }
    return render(request, template_name=template, context=context)

@login_required(login_url='/accounts/login/')
def load_steps(request):
    template = 'project_management/steps_dropdown_list_options.html'
    context = {}    
    id_methodology = request.GET.get('id_methodology')
    steps = Steps.objects.filter(methodology_id=id_methodology).order_by('order')
    context['steps'] = steps
    return render(request, template_name=template,context=context)