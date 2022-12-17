from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AuthorizedUser

# Register your models here.


@admin.register(AuthorizedUser)
class AuthorizedUserAdmin(UserAdmin): pass
