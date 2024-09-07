# Generated by Django 3.1.5 on 2021-01-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0003_deliverable_feedback_person_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='methodology',
            name='steps',
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_1',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 1'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_10',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 10'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_2',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 2'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_3',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 3'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_4',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 4'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_5',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 5'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_6',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 6'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_7',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 7'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_8',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 8'),
        ),
        migrations.AddField(
            model_name='methodology',
            name='step_9',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='Etapa 9'),
        ),
    ]
