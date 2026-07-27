
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur,Candidat,Recruteur


class UtilisateurAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff")

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Candidat)
admin.site.register(Recruteur)