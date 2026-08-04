from django.contrib import admin
from .models import OffreEmploi, Candidature, Candidat

@admin.register(OffreEmploi)
class OffreEmploiAdmin(admin.ModelAdmin):
    list_display = ("titre", "utilisateur", "type_contrat", "mode_travail", "statut_offre", "date_publication")
    list_filter = ("statut_offre", "type_contrat", "mode_travail", "departement")
    search_fields = ("titre", "description", "departement")


@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ("prenom", "nom", "email", "ville", "source_recrutement", "annees_experience")
    list_filter = ("niveau_scolaire", "mobilite", "source_recrutement")
    search_fields = ("nom", "prenom", "email", "competences", "ville")


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ("candidat", "offre", "statut", "note_evaluation", "date_entretien")
    list_filter = ("statut", "note_evaluation")