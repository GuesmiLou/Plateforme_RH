from django import forms
from .models import OffreEmploi, Candidat, Candidature


class OffreEmploiForm(forms.ModelForm):
    class Meta:
        model = OffreEmploi
        fields = [
            "titre",
            "description",
            "lieu",
            "date_debut",
            "date_fin",
            "statut_offre",
        ]
        widgets = {
            "date_debut": forms.DateInput(attrs={"type": "date"}),
            "date_fin": forms.DateInput(attrs={"type": "date"}),
        }


class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            "nom",
            "prenom",
            "email",
            "telephone",
            "date_naissance",
            "niveau_scolaire",
            "mobilite",
            "cv",
        ]
        widgets = {
            "date_naissance": forms.DateInput(attrs={"type": "date"}),
        }


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ["statut"]