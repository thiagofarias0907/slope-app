from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Methodology(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.CharField('Descrição', max_length=250)
    step_1 = models.CharField('Etapa 1', max_length=100, null=True, blank=True)
    step_2 = models.CharField('Etapa 2', max_length=100, null=True, blank=True)
    step_3 = models.CharField('Etapa 3', max_length=100, null=True, blank=True)
    step_4 = models.CharField('Etapa 4', max_length=100, null=True, blank=True)
    step_5 = models.CharField('Etapa 5', max_length=100, null=True, blank=True)
    step_6 = models.CharField('Etapa 6', max_length=100, null=True, blank=True)
    step_7 = models.CharField('Etapa 7', max_length=100, null=True, blank=True)
    step_8 = models.CharField('Etapa 7', max_length=100, null=True, blank=True)
    step_9 = models.CharField('Etapa 9', max_length=100, null=True, blank=True)
    step_10 = models.CharField('Etapa 10', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Metodologia'
        verbose_name_plural = 'Metodologias'

    def __str__(self):
        return self.name
    


class MethodologySteps(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.CharField('Descrição', max_length=250)
    #steps = models.ManyToManyField(Steps, through='MethodologyStepsOrder',through_fields=('step','order'))

    class Meta:
        verbose_name = 'Metodologia'
        verbose_name_plural = 'Metodologias'

    def __str__(self):
        return self.name

class Steps(models.Model):
    name = models.CharField('Nome', max_length=250)
    order = models.SmallIntegerField('Ordem da Etapa')
    methodology = models.ForeignKey(MethodologySteps,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas' 
    
    def __str__(self):
        return str(self.order) + " - " + self.name

class Deliverable(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True, null=True)
    type = models.SmallIntegerField('Tipo')

    class Meta:
        verbose_name = 'Entregável'
        verbose_name_plural = 'Entregáveis'
        ordering = ['id']
        # db_table = ''

    def __str__(self):
        return self.name

# class Feedback(models.Model):
#     name = models.CharField('Nome', max_length=150)
#     description = models.TextField('Descrição', blank=True, null=True)
#     type = models.SmallIntegerField('Tipo')

#     class Meta:
#         verbose_name = 'Feedback'
#         verbose_name_plural = 'Feedbacks'
#         ordering = ['id']
#         # db_table = ''

#     def __str__(self):
#         return self.name


class Person(models.Model):
    OCCUPATION_CHOICES = (
        (1, 'Desenvolvedor'),
        (2, 'Analista de Dados'),
        (3, 'Cientísta de Dados'),
        (4, 'Estatístico'),
        (5, 'Gerente de Projeto'),
    )
    first_name = models.CharField('Nome', max_length=150)
    last_name = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField(null=True)
    occupation = models.SmallIntegerField('cARGO', choices=OCCUPATION_CHOICES)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']
        # db_table = ''

    def __str__(self):
        return self.first_name


class Project(models.Model):
    STATUS_CHOICES = (
        (1, 'Iniciado'),
        (2, 'Em Execução'),
        (3, 'Concluído'),
        (4, 'Inativo'),
    )
    PROG_LANGUAGE_CHOICES = (
        (1, 'Java'),
        (2, 'Python'),
        (3, 'R'),
        (4, 'PHP'),
    )
    DELIVERABLE_CHOICES = (
        (1, 'Planilha'),
        (2, 'Modelo matemático'),
        (3, 'Gráfico'),
        (4, 'API'),
        (5, 'Aplicação Web'),
        (6, 'População de Tabela/View'),
    )
    FEEDBACK_CHOICES = (
        (1, 'Aceito'),
        (2, 'Revisar'),
        (3, 'Rejeitado'),
        (4, 'Não consta'),
    )

    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True, null=True)
    methodology = models.ForeignKey(MethodologySteps, on_delete=models.SET_NULL, null=True)
    step = models.ForeignKey(Steps, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField('Status', choices=STATUS_CHOICES)
    date = models.DateField('Data Registro', auto_now=False, auto_now_add=True)
    last_update = models.DateField('Data Última Atualização', auto_now=False, auto_now_add=True)
    responsible = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    programming_language = models.SmallIntegerField('Linguagem', choices=PROG_LANGUAGE_CHOICES)
    technology = models.CharField('Tecnologia', max_length=150)
    technique = models.TextField('Técnica', blank=True, null=True)
    data_source = models.CharField('Fonte Dados', max_length=150)
    references = models.TextField('Referências', blank=True, null=True)
    objective = models.CharField('Objetivo', max_length=250)
    deliverable = models.SmallIntegerField('Entregável', choices=DELIVERABLE_CHOICES)
    requester = models.CharField('Solicitante', max_length=150)
    requester_sector = models.CharField('Setor do Solicitante', max_length=150)
    # feedback = models.ForeignKey(Feedback, on_delete=models.SET_NULL, null=True)
    feedback = models.SmallIntegerField('Feedback', choices=FEEDBACK_CHOICES)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['id']

    def __str__(self):
        return self.name

class ProjectHistory(models.Model):
    step    = models.ForeignKey(Steps, on_delete=models.DO_NOTHING, null=False) 
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=False)
    date    = models.DateField(auto_now=False, auto_now_add=True) 

    class Meta:
        verbose_name = 'Histórico Projeto'
        verbose_name_plural = 'Histórico de Projetos'
        ordering = ['id']

    def __str__(self):
        return (str(self.step)+str(self.project)+str(self.date))