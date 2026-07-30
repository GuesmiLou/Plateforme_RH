from django.db import models
from users.models import Utilisateur, Candidat, Recruteur
from recrutement.models import OffreEmploi, Candidature


def run():
    user_recruteur = Utilisateur.objects.create_user(
        username="techcorp",
        email="contact@techcorp.tn",
        password="motdepasse123",
        role=Utilisateur.Role.RECRUTEUR,
    )
    recruteur = Recruteur.objects.create(
        utilisateur=user_recruteur,
        nom_entreprise="TechCorp",
        description_entreprise="Entreprise de développement logiciel.",
        secteur_activite="Informatique",
    )
    user_candidat1 = Utilisateur.objects.create_user(
        username="amira",
        email="amira@example.com",
        password="motdepasse123",
        role=Utilisateur.Role.CANDIDAT,
    )
    candidat1 = Candidat.objects.create(
        utilisateur=user_candidat1,
        competences="Python, Django",
        telephone="20123456",
    )

    user_candidat2 = Utilisateur.objects.create_user(
        username="karim",
        email="karim@example.com",
        password="motdepasse123",
        role=Utilisateur.Role.CANDIDAT,
    )
    candidat2 = Candidat.objects.create(
        utilisateur=user_candidat2,
        competences="Java, SQL",
        telephone="21987654",
    )


    offre1 = OffreEmploi.objects.create(
        recruteur=recruteur,
        titre="Développeur Python",
        description="Poste junior en développement Django.",
        lieu="Tunis",
        statut_offre="ouverte",
    )
    offre2 = OffreEmploi.objects.create(
        recruteur=recruteur,
        titre="Data Analyst",
        description="Analyse de données RH.",
        lieu="Sfax",
        statut_offre="ouverte",
    )

    Candidature.objects.create(candidat=candidat1, offre=offre1, statut="en_attente")
    Candidature.objects.create(candidat=candidat2, offre=offre1, statut="acceptee")
    Candidature.objects.create(candidat=candidat1, offre=offre2, statut="refusee")

    print("Données de test créées avec succès.")