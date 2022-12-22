from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AuthorizedUser
from django.utils.translation import ugettext_lazy as _

# Register your models here.


@admin.register(AuthorizedUser)
class AuthorizedUserAdmin(UserAdmin):
    """Custom user admin site settings"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'library_name', 'get_position_display')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)  # email is required hence there will always be a sorting key
