from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class UtilisateurSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Utilisateur
        fields = [
            "username",
            "email",
            "nom_entreprise",
            "description_entreprise",
            "secteur_activite",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Utilisateur.Role.RECRUTEUR
        if commit:
            user.save()
        return user