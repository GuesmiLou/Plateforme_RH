from django import forms
from .models import OffreEmploi, Candidat, Candidature


class OffreEmploiForm(forms.ModelForm):
    class Meta:
        model = OffreEmploi
        fields = [
            "titre",
            "description",
            "lieu",
            "departement",             # NOUVEAU
            "type_contrat",            # NOUVEAU
            "mode_travail",            # NOUVEAU
            "salaire_min",             # NOUVEAU
            "salaire_max",             # NOUVEAU
            "niveau_experience_requis",# NOUVEAU
            "niveau_etudes_requis",    # NOUVEAU
            "nombre_postes",           # NOUVEAU
            "avantages",               # NOUVEAU
            "date_debut",
            "date_fin",
            "date_limite_candidature", # NOUVEAU
            "statut_offre",
        ]
        widgets = {
            "date_debut": forms.DateInput(attrs={"type": "date"}),
            "date_fin": forms.DateInput(attrs={"type": "date"}),
            "date_limite_candidature": forms.DateInput(attrs={"type": "date"}), # Calendrier
        }


class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            "nom",
            "prenom",
            "email",
            "telephone",
            "ville",                   # NOUVEAU
            "date_naissance",
            "niveau_scolaire",
            "mobilite",
            "linkedin_url",            # NOUVEAU
            "annees_experience",       # NOUVEAU
            "competences",             # NOUVEAU
            "source_recrutement",      # NOUVEAU
            "disponibilite",           # NOUVEAU
            "pretention_salariale",    # NOUVEAU
            "lettre_motivation",       # NOUVEAU
            "cv",
            "notes_recruteur",         # NOUVEAU
        ]
        widgets = {
            "date_naissance": forms.DateInput(attrs={"type": "date"}),
            "disponibilite": forms.DateInput(attrs={"type": "date"}), # Calendrier
        }


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = [
            "statut", 
            "note_evaluation",  # NOUVEAU
            "commentaire",      # NOUVEAU
            "date_entretien"    # NOUVEAU
        ]
        widgets = {
            "date_entretien": forms.DateTimeInput(attrs={"type": "datetime-local"}), 
        }