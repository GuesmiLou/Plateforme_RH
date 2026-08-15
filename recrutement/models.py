from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Utilisateur
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError

phone_regex = RegexValidator(
    regex=r'^\+?[0-9\s\-()]{7,20}$',
    message="Le numéro de téléphone doit contenir uniquement des chiffres, espaces, ou les symboles +, -, ()."
)
def validate_date_naissance(value):
    if value and value > date.today():
        raise ValidationError("La date de naissance ne peut pas être située dans le futur.")
    
def validate_date_naissance(value):
    if value and value > date.today():
        raise ValidationError("La date de naissance ne peut pas être située dans le futur.")

class OffreEmploi(models.Model):
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

    class NiveauHierarchique(models.TextChoices):
        JUNIOR = "JUNIOR", "Junior / Débutant"
        CONFIRME = "CONFIRME", "Confirmé / Intermédiaire"
        SENIOR = "SENIOR", "Sénior / Expert"
        LEAD = "LEAD", "Team Lead / Manager"
        DIRECTION = "DIRECTION", "Direction / Cadre Dirigeant"

    class HorairesTravail(models.TextChoices):
        PLEIN_TEMPS = "PLEIN_TEMPS", "Plein temps (35h-40h/semaine)"
        TEMPS_PARTIEL = "TEMPS_PARTIEL", "Temps partiel"
        FLEXIBLE = "FLEXIBLE", "Horaires flexibles / Résultats"
        POSTE_3X8 = "POSTE_3X8", "Travail posté (3x8 / 2x8)"

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    lieu = models.CharField(max_length=100, blank=True)
    departement = models.CharField(max_length=100, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_limite_candidature = models.DateField(null=True, blank=True)
    
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
    niveau_hierarchique = models.CharField(
        max_length=30, choices=NiveauHierarchique.choices, default=NiveauHierarchique.CONFIRME
    )
    horaires_travail = models.CharField(
        max_length=30, choices=HorairesTravail.choices, default=HorairesTravail.PLEIN_TEMPS
    )

    salaire_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    niveau_experience_requis = models.CharField(max_length=100, blank=True)
    niveau_etudes_requis = models.CharField(max_length=100, blank=True)
    nombre_postes = models.PositiveIntegerField(default=1)

    competences_cles = models.TextField(
        blank=True,
        help_text="Entrez les compétences séparées par des virgules avec leur priorité. Ex: Python (Indispensable), Docker (Important), AWS (Souhaitable)"
    )
    langues_requises = models.CharField(max_length=255, blank=True, help_text="Ex: Français (Courant), Anglais (B2 / Technique)")
    outils_technologies = models.CharField(max_length=255, blank=True, help_text="Ex: Git, Jira, PostgreSQL, VS Code")
    avantages = models.TextField(blank=True)

    @property
    def list_competences(self):
        if not self.competences_cles:
            return []
        return [c.strip() for c in self.competences_cles.split(",") if c.strip()]

    @property
    def list_outils(self):
        if not self.outils_technologies:
            return []
        return [o.strip() for o in self.outils_technologies.split(",") if o.strip()]
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

    
    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name="candidats",
        null=True,
        blank=True,
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(
        validators=[phone_regex], 
        max_length=20, 
        blank=True
    )
    date_naissance = models.DateField(
        validators=[validate_date_naissance],
        null=True,
        blank=True
    )
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

    
    numero_dossier = models.CharField(max_length=100, unique=True, editable=False, blank=True)

    note_evaluation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Note globale de 1 à 5",
    )
    commentaire = models.TextField(blank=True, help_text="Notes d'évaluation spécifiques à cette candidature")
    
    
    date_entretien_rh = models.DateTimeField(null=True, blank=True)
    date_entretien_technique = models.DateTimeField(null=True, blank=True)
    def score_compatibilite(self):
        score = 0
        max_score = 100

        
        if self.offre.description and self.candidat.competences:
            competences_candidat = set(c.strip().lower() for c in self.candidat.competences.split(","))
            description_offre = self.offre.description.lower()
            
            matches = [comp for comp in competences_candidat if comp in description_offre]
            if competences_candidat:
                score += int((len(matches) / len(competences_candidat)) * 60)

        
        if self.candidat.ville and self.offre.lieu:
            if self.candidat.ville.lower() == self.offre.lieu.lower() or self.candidat.mobilite:
                score += 20

        
        if self.candidat.pretention_salariale and self.offre.salaire_max:
            if self.candidat.pretention_salariale <= self.offre.salaire_max:
                score += 20

        return min(score, max_score)

    class Meta:
        unique_together = ("candidat", "offre")

    def save(self, *args, **kwargs):
        if not self.numero_dossier:
            count = Candidature.objects.filter(offre=self.offre).count() + 1
            self.numero_dossier = f"OFFRE-{self.offre.id}-{count:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.numero_dossier}] {self.candidat} -> {self.offre.titre} ({self.statut})"