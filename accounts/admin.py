from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm


# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['name', 'email', 'last_login']
    list_filter = ['is_admin']
    ordering = ['last_login']

    fieldsets = (
        (
            None, {
                'fields': ['name', 'email', 'password']
            },
        ),
        (
            'Permissions', {
                'fields': ['is_admin', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions']
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'fields': ['name', 'email', 'password1', 'password2']
            }
        ),
    )

    filter_horizontal = ['groups', 'user_permissions']

    readonly_fields = ['last_login']


admin.site.register(User, UserAdmin)
