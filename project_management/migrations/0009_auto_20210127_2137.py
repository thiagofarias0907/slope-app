# Generated by Django 3.1.5 on 2021-01-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0008_auto_20210127_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
