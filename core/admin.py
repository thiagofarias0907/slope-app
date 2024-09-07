from django.contrib import admin

from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Slope'
admin.site.site_title = 'Slope - Administração'
admin.site.index_title = 'Slope - Administração'