# Generated by Django 3.1.5 on 2021-01-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='methodology',
            name='steps',
            field=models.ManyToManyField(to='project_management.Steps'),
        ),
    ]
