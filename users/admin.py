from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
# Register your models here.
class UserAdmin(BaseUserAdmin):
	list_display = ('email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff')
	search_fields = ('email', 'username', 'first_name', 'last_name')

admin.site.register(models.User, UserAdmin)