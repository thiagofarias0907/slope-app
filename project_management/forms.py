from django import forms

from .models import Project, Person, Deliverable, Methodology, Steps, MethodologySteps, ProjectHistory

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('date', 'feedback','last_update')
        verbose_name = 'Formulário De Projetos'

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('date','last_update')
        verbose_name = 'Formulário De Edição de Projetos'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['step'].queryset = Steps.objects.none()

        if 'methodology' in self.data:
            try:
                methodology_id = int(self.data.get('methodology'))
                self.fields['step'].queryset = Steps.objects.filter(methodology_id=methodology_id).order_by('id')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['step'].queryset = self.instance.methodology.steps_set.order_by('id')



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()
        verbose_name = 'Formulário De Pessoas'

class MethodologyForm(forms.ModelForm):
    class Meta:
        model = Methodology
        exclude = ()
        verbose_name = 'Formulário De Metodologias'

class MethodologyStepsForm(forms.ModelForm):
    class Meta:
        model = MethodologySteps
        exclude = ()
        verbose_name = 'Formulário Metodologia Etapas'

class ProjectHistoryForm(forms.ModelForm):
    class Meta:
        model = ProjectHistory
        exclude = ()
        verbose_name = 'Formulário Histórico Projeto'