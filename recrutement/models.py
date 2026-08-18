from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Utilisateur
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError
import re

phone_regex = RegexValidator(
    regex=r'^\+?[0-9\s\-()]{7,20}$',
    message="Le numéro de téléphone doit contenir uniquement des chiffres, espaces, ou les symboles +, -, ()."
)
def validate_date_naissance(value):
    if value and value > date.today():
        raise ValidationError("La date de naissance ne peut pas être située dans le future.")
    
def validate_date_naissance(value):
    if value and value > date.today():
        raise ValidationError("La date de naissance ne peut pas être située dans le future.")

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
    email = models.EmailField(blank=True, unique=True)
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
        """Returns total score out of 100."""
        return self.score_detail()["total_score"]

    def score_detail(self):
        scores = {
            "competences": 0,  # Max 50 pts
            "localisation": 0, # Max 20 pts
            "salaire": 0,      # Max 15 pts
            "etudes": 0,       # Max 15 pts
            "total_score": 0   # Max 100 pts
        }

        candidat_skills = set(
            s.strip().lower() for s in self.candidat.competences.split(",") if s.strip()
        )
        
        if candidat_skills:
            job_requirements = []
            for comp_str in self.offre.list_competences:
                weight = 1.0  
                if "indispensable" in comp_str.lower():
                    weight = 2.0
                elif "important" in comp_str.lower():
                    weight = 1.5
                
                
                clean_name = re.sub(r"\(.*?\)", "", comp_str).strip().lower()
                if clean_name:
                    job_requirements.append((clean_name, weight))

            
            for tool_str in self.offre.list_outils:
                clean_tool = tool_str.strip().lower()
                if clean_tool:
                    job_requirements.append((clean_tool, 1.0))

            if job_requirements:
                total_weight = sum(weight for _, weight in job_requirements)
                matched_weight = sum(
                    weight for skill_name, weight in job_requirements
                    if any(skill_name in c_skill or c_skill in skill_name for c_skill in candidat_skills)
                )
                scores["competences"] = round((matched_weight / total_weight) * 50)

        
        if self.offre.mode_travail == OffreEmploi.ModeTravail.TELECOMMUTE:
            scores["localisation"] = 20
        elif self.candidat.mobilite:
            scores["localisation"] = 20
        elif self.candidat.ville and self.offre.lieu:
            if self.candidat.ville.strip().lower() == self.offre.lieu.strip().lower():
                scores["localisation"] = 20
            else:
                scores["localisation"] = 5  
        else:
            scores["localisation"] = 10  

        
        if not self.candidat.pretention_salariale or not self.offre.salaire_max:
            scores["salaire"] = 15  
        else:
            candidate_req = float(self.candidat.pretention_salariale)
            job_max = float(self.offre.salaire_max)
            
            if candidate_req <= job_max:
                scores["salaire"] = 15
            elif candidate_req <= job_max * 1.15: 
                scores["salaire"] = 8
            else:
                scores["salaire"] = 0

        
        degree_levels = {
            "bac": 1,
            "licence": 2,
            "master": 3,
            "ingenieur": 3,
            "doctorat": 4,
        }
        cand_level = degree_levels.get(self.candidat.niveau_scolaire, 0)
        
        
        req_text = (self.offre.niveau_etudes_requis or "").lower()
        req_level = 0
        for level_key, level_val in degree_levels.items():
            if level_key in req_text:
                req_level = max(req_level, level_val)

        if cand_level >= req_level or req_level == 0:
            scores["etudes"] = 15
        elif cand_level == req_level - 1:
            scores["etudes"] = 7
        else:
            scores["etudes"] = 0

        scores["total_score"] = min(
            sum([scores["competences"], scores["localisation"], scores["salaire"], scores["etudes"]]), 
            100
        )
        return scores

    class Meta:
        unique_together = ("candidat", "offre")

    def save(self, *args, **kwargs):
        if not self.numero_dossier:
            count = Candidature.objects.filter(offre=self.offre).count() + 1
            self.numero_dossier = f"OFFRE-{self.offre.id}-{count:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.numero_dossier}] {self.candidat} -> {self.offre.titre} ({self.statut})"