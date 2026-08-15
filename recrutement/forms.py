from datetime import date
from django import forms
from .models import OffreEmploi, Candidat, Candidature


class OffreEmploiForm(forms.ModelForm):
    class Meta:
        model = OffreEmploi
        fields = [
            "titre",
            "description",
            "lieu",
            "departement",
            "type_contrat",
            "mode_travail",
            "niveau_hierarchique",
            "horaires_travail",
            "salaire_min",
            "salaire_max",
            "niveau_experience_requis",
            "niveau_etudes_requis",
            "langues_requises",
            "competences_cles",
            "outils_technologies",
            "nombre_postes",
            "avantages",
            "date_debut",
            "date_fin",
            "date_limite_candidature",
            "statut_offre",
        ]
        widgets = {
            "date_debut": forms.DateInput(attrs={"type": "date"}),
            "date_fin": forms.DateInput(attrs={"type": "date"}),
            "date_limite_candidature": forms.DateInput(attrs={"type": "date"}),
            "competences_cles": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Ex: Python (Indispensable), Django (Important), Docker (Souhaitable)"
            }),
            "langues_requises": forms.TextInput(attrs={
                "placeholder": "Ex: Français (Courant), Anglais (B2/Technique)"
            }),
            "outils_technologies": forms.TextInput(attrs={
                "placeholder": "Ex: Git, PostgreSQL, Docker, Linux"
            }),
        }

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            "nom",
            "prenom",
            "email",
            "telephone",
            "ville",                   
            "date_naissance",
            "niveau_scolaire",
            "mobilite",
            "linkedin_url",            
            "annees_experience",       
            "competences",             
            "source_recrutement",      
            "disponibilite",           
            "pretention_salariale",    
            "lettre_motivation",       
            "cv",
            "notes_recruteur",         
        ]
        widgets = {
            "date_naissance": forms.DateInput(attrs={
                "type": "date", 
                "max": date.today().isoformat()
            }),
            "disponibilite": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_date_naissance(self):
        date_naissance = self.cleaned_data.get("date_naissance")
        if date_naissance and date_naissance > date.today():
            raise forms.ValidationError("La date de naissance ne peut pas être dans le futur.")
        return date_naissance


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = [
            "statut", 
            "note_evaluation",  
            "commentaire",      
            "date_entretien_rh",
            "date_entretien_technique",
        ]
        widgets = {
            "date_entretien_rh": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "date_entretien_technique": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }