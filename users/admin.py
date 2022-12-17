from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AuthorizedUser
from django.utils.translation import ugettext_lazy as _

# Register your models here.


@admin.register(AuthorizedUser)
class AuthorizedUserAdmin(UserAdmin): pass
