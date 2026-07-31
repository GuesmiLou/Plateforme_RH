
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur


class UtilisateurAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff")

admin.site.register(Utilisateur, UtilisateurAdmin)
