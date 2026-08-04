from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Utilisateur


class OffreEmploi(models.Model):
    # --- Nouvelles classes de choix ---
    class TypeContrat(models.TextChoices):
        CDI = "CDI", "CDI"
        CDD = "CDD", "CDD"
        STAGE = "STAGE", "Stage"
        FREELANCE = "FREELANCE", "Freelance"
        ALTERNANCE = "ALTERNANCE", "Alternance"

    class ModeTravail(models.TextChoices):
        PRESENTIEL = "PRESENTIEL", "Présentiel"
        HYBRIDE = "HYBRIDE", "Hybride"
        TELECOMMUTE = "TELECOMMUTE", "Télétravail"

    
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    lieu = models.CharField(max_length=100, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    statut_offre = models.CharField(
        max_length=20,
        choices=[("ouverte", "Ouverte"), ("fermee", "Fermée")],
        default="ouverte",
    )

    
    type_contrat = models.CharField(
        max_length=20, choices=TypeContrat.choices, default=TypeContrat.CDI
    )
    mode_travail = models.CharField(
        max_length=20, choices=ModeTravail.choices, default=ModeTravail.PRESENTIEL
    )
    salaire_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    niveau_experience_requis = models.CharField(max_length=100, blank=True)
    niveau_etudes_requis = models.CharField(max_length=100, blank=True)
    nombre_postes = models.PositiveIntegerField(default=1)
    date_limite_candidature = models.DateField(null=True, blank=True)
    departement = models.CharField(max_length=100, blank=True)
    avantages = models.TextField(blank=True)

    def __str__(self):
        return self.titre


class Candidat(models.Model):
    
    class NiveauScolaire(models.TextChoices):
        BAC = "bac", "Baccalauréat"
        LICENCE = "licence", "Licence"
        MASTER = "master", "Master"
        INGENIEUR = "ingenieur", "Ingénieur"
        DOCTORAT = "doctorat", "Doctorat"

    class SourceRecrutement(models.TextChoices):
        SITE_CARRIERE = "SITE_CARRIERE", "Site Carrière"
        LINKEDIN = "LINKEDIN", "LinkedIn"
        RECOMMANDATION = "RECOMMANDATION", "Recommandation"
        AUTRE = "AUTRE", "Autre"

    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    niveau_scolaire = models.CharField(max_length=20, choices=NiveauScolaire.choices, blank=True)
    mobilite = models.BooleanField(default=False, help_text="Le candidat est-il mobile géographiquement ?")
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)

    
    ville = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    annees_experience = models.PositiveIntegerField(default=0)
    competences = models.TextField(blank=True, help_text="Liste de mots-clés ou compétences")
    source_recrutement = models.CharField(
        max_length=30, choices=SourceRecrutement.choices, default=SourceRecrutement.SITE_CARRIERE
    )
    disponibilite = models.DateField(null=True, blank=True)
    pretention_salariale = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lettre_motivation = models.TextField(blank=True)
    notes_recruteur = models.TextField(blank=True, help_text="Notes internes (masquées au candidat)")

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Candidature(models.Model):
    
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    offre = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE)
    date_candidature = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ("en_attente", "En attente"),
            ("acceptee", "Acceptée"),
            ("refusee", "Refusée"),
        ],
        default="en_attente",
    )

    
    note_evaluation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Note globale de 1 à 5",
    )
    commentaire = models.TextField(blank=True, help_text="Notes d'évaluation spécifiques à cette candidature")
    date_entretien = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.candidat} -> {self.offre.titre} ({self.statut})"