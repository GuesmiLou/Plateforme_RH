from datetime import date
from users.models import Utilisateur
from recrutement.models import OffreEmploi, Candidat, Candidature


def run():
    entreprise1 = Utilisateur.objects.create_user(
        username="simac",
        email="contact@simac.tn",
        password="motdepasse123",
        nom_entreprise="Simac",
        description_entreprise="Entreprise industrielle.",
        secteur_activite="Industrie",
    )

    offre1 = OffreEmploi.objects.create(
        utilisateur=entreprise1,
        titre="Technicien de maintenance",
        description="Maintenance des équipements industriels.",
        lieu="Tunis",
        date_debut=date(2026, 8, 1),
        date_fin=date(2026, 8, 31),
        statut_offre="ouverte",
    )

    offre2 = OffreEmploi.objects.create(
        utilisateur=entreprise1,
        titre="Développeur Python",
        description="Poste junior en développement Django.",
        lieu="Sfax",
        date_debut=date(2026, 9, 1),
        date_fin=date(2026, 9, 30),
        statut_offre="ouverte",
    )

    candidat1 = Candidat.objects.create(
        nom="Ben Ali",
        prenom="Amira",
        email="amira@example.com",
        telephone="20123456",
        date_naissance=date(1998, 4, 12),
        niveau_scolaire="licence",
        mobilite=True,
    )

    candidat2 = Candidat.objects.create(
        nom="Trabelsi",
        prenom="Karim",
        email="karim@example.com",
        telephone="21987654",
        date_naissance=date(1995, 11, 3),
        niveau_scolaire="ingenieur",
        mobilite=False,
    )

    Candidature.objects.create(candidat=candidat1, offre=offre1, statut="en_attente")
    Candidature.objects.create(candidat=candidat2, offre=offre2, statut="acceptee")
    Candidature.objects.create(candidat=candidat1, offre=offre2, statut="refusee")

    print("Données de test créées avec succès.")