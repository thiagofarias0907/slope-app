# Generated by Django 3.1.5 on 2021-03-12 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0017_auto_20210225_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date_atualizacao',
            new_name='last_update',
        ),
    ]
