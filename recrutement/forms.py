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
            "salaire_min",            
            "salaire_max",            
            "niveau_experience_requis",
            "niveau_etudes_requis",    
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
            "date_naissance": forms.DateInput(attrs={"type": "date"}),
            "disponibilite": forms.DateInput(attrs={"type": "date"}),
        }


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