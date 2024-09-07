from django.contrib import admin
from .models import Person, Project, Deliverable


# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['user', 'occupation']

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Deliverable)
