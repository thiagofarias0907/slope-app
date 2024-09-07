from django.urls import path

app_name = 'project_management'

from . import views

urlpatterns = [
    path('all_projects/', views.show_projects, name='management'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:id_project>/', views.edit_project, name='edit_project'),
    path('ajax/load-steps/', views.load_steps, name='ajax_load_steps'),
    path('delete_project/<int:id_project>/', views.delete_project, name='delete_project'),
    path('add_methodology/', views.add_methodologies_and_steps, name='add_methodology'),
    path('all_methodologies/', views.show_methodologies_steps, name='all_methodologies'),
    path('edit_methodology/<int:id_methodology>/', views.edit_methodologies_and_steps, name='edit_methodology'),
    path('delete_methodology/<int:id_methodology>/', views.delete_methodology_steps, name='delete_methodology'),
    path('team_members/', views.show_team_members, name='all_team_members'),
    path('add_team_member/', views.add_person, name='add_team_member'),
    path('edit_team_member/<int:id_person>/', views.edit_person, name='edit_team_member'),
    path('delete_team_member/<int:id_person>/', views.delete_person, name='delete_team_member'),

]