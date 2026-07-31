from django.db import models
from users.models import Utilisateur


class OffreEmploi(models.Model):
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

    def __str__(self):
        return self.titre


class Candidat(models.Model):
    class NiveauScolaire(models.TextChoices):
        BAC = "bac", "Baccalauréat"
        LICENCE = "licence", "Licence"
        MASTER = "master", "Master"
        INGENIEUR = "ingenieur", "Ingénieur"
        DOCTORAT = "doctorat", "Doctorat"

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    niveau_scolaire = models.CharField(max_length=20, choices=NiveauScolaire.choices, blank=True)
    mobilite = models.BooleanField(default=False, help_text="Le candidat est-il mobile géographiquement ?")
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)

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

    def __str__(self):
        return f"{self.candidat} -> {self.offre.titre} ({self.statut})"