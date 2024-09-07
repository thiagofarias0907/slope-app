# Generated by Django 3.1.5 on 2021-03-12 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0018_auto_20210311_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project_management.project')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project_management.steps')),
            ],
            options={
                'verbose_name': 'Histórico Projeto',
                'verbose_name_plural': 'Histórico de Projetos',
                'ordering': ['id'],
            },
        ),
    ]
