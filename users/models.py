from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):

    class Role(models.TextChoices):
        RECRUTEUR = "recruteur", "Recruteur"
        ADMIN = "admin", "Administrateur"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.RECRUTEUR
    )
    date_inscription = models.DateTimeField(auto_now_add=True)

    nom_entreprise = models.CharField(max_length=255, blank=True)
    description_entreprise = models.TextField(blank=True)
    secteur_activite = models.CharField(max_length=100, blank=True)
    site_web = models.URLField(max_length=255, blank=True)
    adresse_entreprise = models.CharField(max_length=255, blank=True)
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_entreprise or self.username} ({self.role})"