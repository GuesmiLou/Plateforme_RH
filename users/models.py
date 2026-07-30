from django.contrib.auth.models import AbstractUser
from django.db import models
class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        CANDIDAT = "candidat", "Candidat"
        RECRUTEUR = "recruteur", "Recruteur"
        ADMIN = "admin", "Administrateur"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices,  default=Role.ADMIN)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"
class Candidat(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE,primary_key=True)
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)
    competences = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
 
    def __str__(self):
        return f"Candidat: {self.utilisateur.username}"
class Recruteur(models.Model):
    utilisateur = models.OneToOneField(
        Utilisateur,on_delete= models.CASCADE,primary_key="True"
    )
    nom_entreprise = models.CharField(max_length=255)
    description_entreprise = models.TextField(blank=True)
    secteur_activite = models.CharField(max_length=200, blank=True)
 
    def __str__(self):
        return f"Recruteur: {self.nom_entreprise} ({self.utilisateur.username})"
