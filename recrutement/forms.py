from django import forms
from .models import OffreEmploi, Candidature


class OffreEmploiForm(forms.ModelForm):
    class Meta:
        model = OffreEmploi
        fields = ["titre", "description", "lieu", "statut_offre"]


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ["statut"]