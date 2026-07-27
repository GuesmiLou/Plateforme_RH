from django.db import models
from users.models import Candidat, Recruteur


class OffreEmploi(models.Model):
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    lieu = models.CharField(max_length=100, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    statut_offre = models.CharField(
        max_length=20,
        choices=[("ouverte", "Ouverte"), ("fermee", "Fermée")],
        default="ouverte",
    )

    def __str__(self):
        return self.titre


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