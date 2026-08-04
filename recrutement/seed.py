from datetime import date, datetime
from django.utils import timezone
from users.models import Utilisateur
from recrutement.models import OffreEmploi, Candidat, Candidature


def run():
    Candidature.objects.all().delete()
    Candidat.objects.all().delete()
    OffreEmploi.objects.all().delete()
    user, created = Utilisateur.objects.get_or_create(
        username="simac",
        defaults={
            "email": "contact@simac.tn",
            "nom_entreprise": "Simac",
            "description_entreprise": "Entreprise industrielle.",
            "secteur_activite": "Industrie",
            "role": Utilisateur.Role.RECRUTEUR,
        }
    )
    if created:
        user.set_password("motdepasse123")
        user.save()

    offre1 = OffreEmploi.objects.create(
        utilisateur=user,
        titre="Technicien de maintenance",
        description="Maintenance préventive et curative des équipements industriels.",
        lieu="Tunis",
        departement="Maintenance & Production",
        type_contrat=OffreEmploi.TypeContrat.CDI,
        mode_travail=OffreEmploi.ModeTravail.PRESENTIEL,
        salaire_min=1200.00,
        salaire_max=1600.00,
        niveau_experience_requis="2 à 5 ans",
        niveau_etudes_requis="Bac +2 / BTS",
        nombre_postes=2,
        avantages="Tickets restaurant, prime de rendement, assurance groupe.",
        date_debut=date(2026, 8, 1),
        date_fin=date(2026, 8, 31),
        date_limite_candidature=date(2026, 7, 25),
        statut_offre="ouverte",
    )

    offre2 = OffreEmploi.objects.create(
        utilisateur=user,
        titre="Développeur Python / Django",
        description="Développement et tierce maintenance applicative sur plateformes Web.",
        lieu="Sfax",
        departement="Informatique & R&D",
        type_contrat=OffreEmploi.TypeContrat.CDI,
        mode_travail=OffreEmploi.ModeTravail.HYBRIDE,
        salaire_min=2500.00,
        salaire_max=3500.00,
        niveau_experience_requis="Junior (1-2 ans)",
        niveau_etudes_requis="Bac +5 / Diplôme d'Ingénieur",
        nombre_postes=1,
        avantages="Horaires flexibles, budget formation, PC portable fourni.",
        date_debut=date(2026, 9, 1),
        date_fin=date(2026, 9, 30),
        date_limite_candidature=date(2026, 8, 20),
        statut_offre="ouverte",
    )

    
    candidat1 = Candidat.objects.create(
        nom="Ben Ali",
        prenom="Amira",
        email="amira@example.com",
        telephone="20123456",
        ville="Tunis",
        date_naissance=date(1998, 4, 12),
        niveau_scolaire=Candidat.NiveauScolaire.LICENCE,
        mobilite=True,
        linkedin_url="https://linkedin.com/in/amira-benali",
        annees_experience=3,
        competences="Maintenance mécanique, Automatisme, Pneumatique, TPM",
        source_recrutement=Candidat.SourceRecrutement.LINKEDIN,
        disponibilite=date(2026, 8, 1),
        pretention_salariale=1400.00,
        lettre_motivation="Récemment diplômée avec 3 ans d'expérience en usine...",
        notes_recruteur="Excellente communication, disponible immédiatement.",
    )

    candidat2 = Candidat.objects.create(
        nom="Trabelsi",
        prenom="Karim",
        email="karim@example.com",
        telephone="21987654",
        ville="Sfax",
        date_naissance=date(1995, 11, 3),
        niveau_scolaire=Candidat.NiveauScolaire.INGENIEUR,
        mobilite=False,
        linkedin_url="https://linkedin.com/in/karim-trabelsi",
        annees_experience=2,
        competences="Python, Django, PostgreSQL, Docker, Git, REST API",
        source_recrutement=Candidat.SourceRecrutement.SITE_CARRIERE,
        disponibilite=date(2026, 9, 15),
        pretention_salariale=3000.00,
        lettre_motivation="Passionné par le développement Backend Django...",
        notes_recruteur="Bon profil technique, prétentions salariales alignées.",
    )

    
    Candidature.objects.create(
        candidat=candidat1,
        offre=offre1,
        statut="en_attente",
        note_evaluation=4,
        commentaire="Profil très intéressant pour le poste de technicien.",
        date_entretien=timezone.make_aware(datetime(2026, 8, 10, 10, 0)),
    )

    Candidature.objects.create(
        candidat=candidat2,
        offre=offre2,
        statut="acceptee",
        note_evaluation=5,
        commentaire="Test technique réussi avec succès (95/100).",
        date_entretien=timezone.make_aware(datetime(2026, 8, 5, 14, 30)),
    )

    Candidature.objects.create(
        candidat=candidat1,
        offre=offre2,
        statut="refusee",
        note_evaluation=2,
        commentaire="Manque de compétences en développement logiciel.",
    )

    print("Données de test ATS / Schema.org générées avec succès.")