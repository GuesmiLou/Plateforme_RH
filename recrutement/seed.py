from datetime import date, datetime
from django.utils import timezone
from users.models import Utilisateur
from recrutement.models import OffreEmploi, Candidat, Candidature


def run():
    user, created = Utilisateur.objects.get_or_create(
        username="simac",
        defaults={
            "email": "contact@simac.tn",
            "nom_entreprise": "Simac",
            "description_entreprise": "Entreprise leader dans l'industrie et la transformation numérique.",
            "secteur_activite": "Industrie & Technologie",
            "role": Utilisateur.Role.RECRUTEUR,
            "site_web": "https://www.simac.tn",
            "adresse_entreprise": "Zone Industrielle, Charguia I, Tunis",
        }
    )
    if created:
        user.set_password("motdepasse123")
        user.save()

    offres_data = [
        {
            "titre": "Technicien de maintenance industrielle",
            "description": "Maintenance préventive et curative des équipements industriels et des lignes d'assemblage.",
            "lieu": "Tunis",
            "departement": "Maintenance & Production",
            "type_contrat": OffreEmploi.TypeContrat.CDI,
            "mode_travail": OffreEmploi.ModeTravail.PRESENTIEL,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.CONFIRME,
            "horaires_travail": OffreEmploi.HorairesTravail.POSTE_3X8,
            "salaire_min": 1200.00,
            "salaire_max": 1600.00,
            "niveau_experience_requis": "2 à 5 ans",
            "niveau_etudes_requis": "Bac +2 / BTS Électromécanique",
            "langues_requises": "Français (Courant), Arabe (Maternelle)",
            "competences_cles": "Automatisme Siemens (Indispensable), Électromécanique (Indispensable), Pneumatique (Important), Diagnostic de panne (Indispensable)",
            "outils_technologies": "GMAO, Multimètre, Automates S7-1200, Schémas électriques",
            "nombre_postes": 2,
            "avantages": "Tickets restaurant, prime de rendement, assurance groupe 100%.",
            "date_debut": date(2026, 9, 1),
            "date_fin": date(2026, 9, 30),
            "date_limite_candidature": date(2026, 8, 25),
            "statut_offre": "ouverte",
        },
        {
            "titre": "Développeur Python / Django Fullstack",
            "description": "Conception, développement et tierce maintenance applicative sur nos plateformes Web RH.",
            "lieu": "Sfax",
            "departement": "Informatique & R&D",
            "type_contrat": OffreEmploi.TypeContrat.CDI,
            "mode_travail": OffreEmploi.ModeTravail.HYBRIDE,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.JUNIOR,
            "horaires_travail": OffreEmploi.HorairesTravail.FLEXIBLE,
            "salaire_min": 2500.00,
            "salaire_max": 3500.00,
            "niveau_experience_requis": "Junior (1-2 ans)",
            "niveau_etudes_requis": "Bac +5 / Diplôme d'Ingénieur en Informatique",
            "langues_requises": "Français (Courant), Anglais (Professionnel / B2)",
            "competences_cles": "Python 3 (Indispensable), Django Framework (Indispensable), PostgreSQL (Important), REST APIs (Important), Docker (Souhaitable)",
            "outils_technologies": "Git, Docker, VS Code, Linux, Postman, Jira",
            "nombre_postes": 1,
            "avantages": "Horaires flexibles, télétravail 2j/sem, budget formation, PC portable.",
            "date_debut": date(2026, 9, 15),
            "date_fin": date(2026, 10, 15),
            "date_limite_candidature": date(2026, 8, 30),
            "statut_offre": "ouverte",
        },
        {
            "titre": "Ingénieur Qualité & Sécurité Industrielle (HSE)",
            "description": "Supervision des normes ISO 9001/14001, réalisation des audits internes et prévention des risques au sein des ateliers.",
            "lieu": "Sousse",
            "departement": "Qualité & Sécurité",
            "type_contrat": OffreEmploi.TypeContrat.CDI,
            "mode_travail": OffreEmploi.ModeTravail.PRESENTIEL,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.CONFIRME,
            "horaires_travail": OffreEmploi.HorairesTravail.PLEIN_TEMPS,
            "salaire_min": 2200.00,
            "salaire_max": 2800.00,
            "niveau_experience_requis": "3 à 5 ans",
            "niveau_etudes_requis": "Bac +5 / Ingénieur Qualité ou Génie Industriel",
            "langues_requises": "Français (Courant), Anglais (Technique)",
            "competences_cles": "Normes ISO 9001 (Indispensable), Audit Qualité (Indispensable), Gestion des risques HSE (Important), 5S / Lean (Souhaitable)",
            "outils_technologies": "Excel avancé, SAP QMS, Outils résolution de problèmes (Ishikawa, 5P)",
            "nombre_postes": 1,
            "avantages": "Voiture de service, assurance groupe, prime annuelle d'objectif.",
            "date_debut": date(2026, 10, 1),
            "date_fin": date(2026, 11, 1),
            "date_limite_candidature": date(2026, 9, 15),
            "statut_offre": "ouverte",
        },
        {
            "titre": "Responsable Ressources Humaines",
            "description": "Pilotage du recrutement, de la paie, des relations sociales et du développement des compétences.",
            "lieu": "Tunis",
            "departement": "Ressources Humaines",
            "type_contrat": OffreEmploi.TypeContrat.CDI,
            "mode_travail": OffreEmploi.ModeTravail.PRESENTIEL,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.SENIOR,
            "horaires_travail": OffreEmploi.HorairesTravail.PLEIN_TEMPS,
            "salaire_min": 3200.00,
            "salaire_max": 4200.00,
            "niveau_experience_requis": "5 à 8 ans",
            "niveau_etudes_requis": "Bac +5 / Master RH ou Droit du travail",
            "langues_requises": "Français (Bilingue), Arabe (Maternelle)",
            "competences_cles": "Droit du travail tunisien (Indispensable), Gestion de la paie (Indispensable), Recrutement ATS (Important), Management (Important)",
            "outils_technologies": "ERP Paie, Sage HRMS, Pack Office, ATS Django",
            "nombre_postes": 1,
            "avantages": "Téléphone de fonction, treizième mois, mutuelle santé haut de gamme.",
            "date_debut": date(2026, 9, 1),
            "date_fin": date(2026, 10, 1),
            "date_limite_candidature": date(2026, 8, 28),
            "statut_offre": "ouverte",
        },
        {
            "titre": "Chef de Projet Systèmes Embarqués",
            "description": "Coordination technique et fonctionnelle des projets R&D sur calculateurs électroniques automobile et industriel.",
            "lieu": "Tunis",
            "departement": "Informatique & R&D",
            "type_contrat": OffreEmploi.TypeContrat.CDI,
            "mode_travail": OffreEmploi.ModeTravail.HYBRIDE,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.LEAD,
            "horaires_travail": OffreEmploi.HorairesTravail.FLEXIBLE,
            "salaire_min": 3800.00,
            "salaire_max": 5000.00,
            "niveau_experience_requis": "5+ ans",
            "niveau_etudes_requis": "Bac +5 / Ingénieur Électronique ou Embarqué",
            "langues_requises": "Anglais (Courant / C1), Français (Courant)",
            "competences_cles": "C/C++ Embarqué (Indispensable), Protocoles CAN/LIN (Indispensable), Gestion de projet Agile (Important), Microcontrôleurs STM32 (Important)",
            "outils_technologies": "Git, JIRA, Oscilloscope, Vector CANoe, Keil MDK",
            "nombre_postes": 1,
            "avantages": "Prime sur objectif, PC haute performance, déplacements pris en charge.",
            "date_debut": date(2026, 10, 15),
            "date_fin": date(2026, 11, 30),
            "date_limite_candidature": date(2026, 9, 30),
            "statut_offre": "ouverte",
        },
        {
            "titre": "Gestionnaire Supply Chain & Logistique",
            "description": "Gestion des approvisionnements, optimisation des stocks et coordination avec les transporteurs internationaux.",
            "lieu": "Bizerte",
            "departement": "Logistique & Achat",
            "type_contrat": OffreEmploi.TypeContrat.CDD,
            "mode_travail": OffreEmploi.ModeTravail.PRESENTIEL,
            "niveau_hierarchique": OffreEmploi.NiveauHierarchique.CONFIRME,
            "horaires_travail": OffreEmploi.HorairesTravail.PLEIN_TEMPS,
            "salaire_min": 1800.00,
            "salaire_max": 2300.00,
            "niveau_experience_requis": "2 à 4 ans",
            "niveau_etudes_requis": "Bac +3 / Licence Commerce International ou Logistique",
            "langues_requises": "Français (Courant), Anglais (Bon niveau)",
            "competences_cles": "Gestion des stocks (Indispensable), Procédures douanières (Important), Négociation fournisseurs (Important)",
            "outils_technologies": "SAP MM, Excel avancé, Douane en ligne TTN",
            "nombre_postes": 1,
            "avantages": "Cantine d'entreprise, transport assuré, possibilité de conversion en CDI.",
            "date_debut": date(2026, 9, 1),
            "date_fin": date(2026, 12, 31),
            "date_limite_candidature": date(2026, 8, 25),
            "statut_offre": "ouverte",
        }
    ]

    offres = {}
    for data in offres_data:
        titre = data.pop("titre")
        offre_obj, _ = OffreEmploi.objects.update_or_create(
            utilisateur=user,
            titre=titre,
            defaults=data
        )
        offres[titre] = offre_obj

    # 3. Base de candidats
    candidats_data = [
        {
            "nom": "Ben Ali",
            "prenom": "Amira",
            "email": "amira.benali@example.com",
            "telephone": "+216 20123456",
            "ville": "Tunis",
            "date_naissance": date(1998, 4, 12),
            "niveau_scolaire": Candidat.NiveauScolaire.LICENCE,
            "mobilite": True,
            "linkedin_url": "https://linkedin.com/in/amira-benali",
            "annees_experience": 3,
            "competences": "Automatisme Siemens, Électromécanique, Maintenance mécanique, Pneumatique, TPM, Diagnostic de panne",
            "source_recrutement": Candidat.SourceRecrutement.LINKEDIN,
            "disponibilite": date(2026, 8, 20),
            "pretention_salariale": 1500.00,
            "lettre_motivation": "Technicienne rigoureuse avec 3 ans d'expérience sur lignes d'assemblage automatisées.",
            "notes_recruteur": "Très bon profil opérationnel, réactive et mobile sur tout le grand Tunis.",
        },
        {
            "nom": "Trabelsi",
            "prenom": "Karim",
            "email": "karim.trabelsi@example.com",
            "telephone": "+216 21987654",
            "ville": "Sfax",
            "date_naissance": date(1995, 11, 3),
            "niveau_scolaire": Candidat.NiveauScolaire.INGENIEUR,
            "mobilite": False,
            "linkedin_url": "https://linkedin.com/in/karim-trabelsi",
            "annees_experience": 2,
            "competences": "Python 3, Django Framework, PostgreSQL, REST APIs, Git, Docker",
            "source_recrutement": Candidat.SourceRecrutement.SITE_CARRIERE,
            "disponibilite": date(2026, 9, 15),
            "pretention_salariale": 3000.00,
            "lettre_motivation": "Développeur passionné par la conception d'architectures web robustes en Django.",
            "notes_recruteur": "Excellentes compétences techniques, code propre et structuré.",
        },
        {
            "nom": "Gharbi",
            "prenom": "Yassine",
            "email": "yassine.gharbi@example.com",
            "telephone": "+216 55443322",
            "ville": "Tunis",
            "date_naissance": date(1992, 6, 25),
            "niveau_scolaire": Candidat.NiveauScolaire.INGENIEUR,
            "mobilite": True,
            "linkedin_url": "https://linkedin.com/in/yassine-gharbi",
            "annees_experience": 6,
            "competences": "C/C++ Embarqué, Protocoles CAN/LIN, STM32, Microcontrôleurs, JIRA, Git, Vector CANoe",
            "source_recrutement": Candidat.SourceRecrutement.LINKEDIN,
            "disponibilite": date(2026, 10, 1),
            "pretention_salariale": 4200.00,
            "lettre_motivation": "Ingénieur Senior spécialisé dans le logiciel embarqué automobile et la conduite de projets.",
            "notes_recruteur": "Excellente maîtrise technique. Idéal pour piloter l'équipe R&D.",
        },
        {
            "nom": "Mansouri",
            "prenom": "Sarra",
            "email": "sarra.mansouri@example.com",
            "telephone": "+216 98112233",
            "ville": "Sousse",
            "date_naissance": date(1996, 1, 15),
            "niveau_scolaire": Candidat.NiveauScolaire.MASTER,
            "mobilite": False,
            "linkedin_url": "https://linkedin.com/in/sarra-mansouri",
            "annees_experience": 4,
            "competences": "Normes ISO 9001, Audit Qualité, Gestion des risques HSE, 5S / Lean, Audit interne",
            "source_recrutement": Candidat.SourceRecrutement.RECOMMANDATION,
            "disponibilite": date(2026, 9, 1),
            "pretention_salariale": 2400.00,
            "lettre_motivation": "Auditrice qualité certifiée, motivée par le maintien des standards d'excellence industrielle.",
            "notes_recruteur": "Profil solide, recommandée par un ancien collaborateur.",
        },
        {
            "nom": "Chaabane",
            "prenom": "Olfa",
            "email": "olfa.chaabane@example.com",
            "telephone": "+216 22334455",
            "ville": "Tunis",
            "date_naissance": date(1990, 8, 30),
            "niveau_scolaire": Candidat.NiveauScolaire.MASTER,
            "mobilite": False,
            "linkedin_url": "https://linkedin.com/in/olfa-chaabane",
            "annees_experience": 7,
            "competences": "Droit du travail tunisien, Gestion de la paie, Recrutement ATS, Sage HRMS, Management RH",
            "source_recrutement": Candidat.SourceRecrutement.SITE_CARRIERE,
            "disponibilite": date(2026, 9, 1),
            "pretention_salariale": 3800.00,
            "lettre_motivation": "Responsable RH avec 7 ans d'expérience dans la gestion du personnel en milieu industriel.",
            "notes_recruteur": "Aisance relationnelle, très bonne maîtrise du cadre juridique.",
        },
        {
            "nom": "Triki",
            "prenom": "Mohamed",
            "email": "mohamed.triki@example.com",
            "telephone": "+216 25667788",
            "ville": "Bizerte",
            "date_naissance": date(1997, 3, 18),
            "niveau_scolaire": Candidat.NiveauScolaire.LICENCE,
            "mobilite": True,
            "linkedin_url": "https://linkedin.com/in/mohamed-triki",
            "annees_experience": 3,
            "competences": "Gestion des stocks, Procédures douanières, SAP MM, Logistique internationale, TTN",
            "source_recrutement": Candidat.SourceRecrutement.AUTRE,
            "disponibilite": date(2026, 8, 25),
            "pretention_salariale": 2000.00,
            "lettre_motivation": "Gestionnaire logistique avec expérience en douane et suivi de marchandises import/export.",
            "notes_recruteur": "Pratique courante de SAP MM, disponible immédiatement.",
        },
        {
            "nom": "Louati",
            "prenom": "Bilel",
            "email": "bilel.louati@example.com",
            "telephone": "+216 50114477",
            "ville": "Sfax",
            "date_naissance": date(1999, 9, 9),
            "niveau_scolaire": Candidat.NiveauScolaire.BAC,
            "mobilite": True,
            "linkedin_url": "",
            "annees_experience": 1,
            "competences": "Électromécanique, Schémas électriques, Multimètre, Maintenance de premier niveau",
            "source_recrutement": Candidat.SourceRecrutement.SITE_CARRIERE,
            "disponibilite": date(2026, 8, 20),
            "pretention_salariale": 1100.00,
            "lettre_motivation": "Jeune diplômé motivated pour intégrer une grande structure industrielle.",
            "notes_recruteur": "Enthousiaste mais manque encore d'expérience sur les automates Siemens.",
        },
        {
            "nom": "Dridi",
            "prenom": "Hamza",
            "email": "hamza.dridi@example.com",
            "telephone": "+216 29881122",
            "ville": "Tunis",
            "date_naissance": date(2001, 2, 14),
            "niveau_scolaire": Candidat.NiveauScolaire.LICENCE,
            "mobilite": False,
            "linkedin_url": "https://linkedin.com/in/hamza-dridi",
            "annees_experience": 1,
            "competences": "Python 3, Django, HTML/CSS, Git, MySQL, JavaScript",
            "source_recrutement": Candidat.SourceRecrutement.LINKEDIN,
            "disponibilite": date(2026, 9, 1),
            "pretention_salariale": 2200.00,
            "lettre_motivation": "Développeur Junior curieux, ayant réalisé plusieurs projets académiques sous Django.",
            "notes_recruteur": "Potentiel intéressant pour un poste Junior.",
        }
    ]

    candidats = {}
    for data in candidats_data:
        email = data.pop("email")
        cand_obj, _ = Candidat.objects.update_or_create(
            utilisateur=user,
            email=email,
            defaults=data
        )
        candidats[email] = cand_obj

    # 4. Candidatures & Évaluations ATS
    candidatures_data = [
        # Technicien Maintenance
        {
            "candidat_email": "amira.benali@example.com",
            "offre_titre": "Technicien de maintenance industrielle",
            "statut": "acceptee",
            "note_evaluation": 5,
            "commentaire": "Excellente maîtrise des automates Siemens. Entretien technique réussi avec brio.",
            "date_rh": datetime(2026, 8, 10, 10, 0),
            "date_tech": datetime(2026, 8, 12, 14, 0),
        },
        {
            "candidat_email": "bilel.louati@example.com",
            "offre_titre": "Technicien de maintenance industrielle",
            "statut": "en_attente",
            "note_evaluation": 3,
            "commentaire": "Profil junior acceptable. Prévoir une évaluation pratique sur automate.",
            "date_rh": datetime(2026, 8, 18, 11, 30),
            "date_tech": None,
        },

        # Développeur Python / Django
        {
            "candidat_email": "karim.trabelsi@example.com",
            "offre_titre": "Développeur Python / Django Fullstack",
            "statut": "acceptee",
            "note_evaluation": 5,
            "commentaire": "Test technique exécuté avec 95% de réussite. Prétentions dans la fourchette.",
            "date_rh": datetime(2026, 8, 5, 11, 0),
            "date_tech": datetime(2026, 8, 7, 14, 30),
        },
        {
            "candidat_email": "hamza.dridi@example.com",
            "offre_titre": "Développeur Python / Django Fullstack",
            "statut": "en_attente",
            "note_evaluation": 4,
            "commentaire": "Bon niveau théorique. À convoquer pour l'entretien technique.",
            "date_rh": datetime(2026, 8, 15, 0, 0),
            "date_tech": None,
        },
        {
            "candidat_email": "amira.benali@example.com",
            "offre_titre": "Développeur Python / Django Fullstack",
            "statut": "refusee",
            "note_evaluation": 1,
            "commentaire": "Profil orienté maintenance mécanique, non adéquat pour le développement web.",
            "date_rh": None,
            "date_tech": None,
        },

        # Chef de Projet Embarqué
        {
            "candidat_email": "yassine.gharbi@example.com",
            "offre_titre": "Chef de Projet Systèmes Embarqués",
            "statut": "en_attente",
            "note_evaluation": 5,
            "commentaire": "Superbe CV. Solides références en CAN/LIN et gestion d'équipe.",
            "date_rh": datetime(2026, 8, 20, 15, 0),
            "date_tech": datetime(2026, 8, 22, 10, 0),
        },

        # Qualité & HSE
        {
            "candidat_email": "sarra.mansouri@example.com",
            "offre_titre": "Ingénieur Qualité & Sécurité Industrielle (HSE)",
            "statut": "acceptee",
            "note_evaluation": 5,
            "commentaire": "Excellente connaissance de l'ISO 9001. Validée par le responsable d'usine.",
            "date_rh": datetime(2026, 8, 8, 9, 30),
            "date_tech": datetime(2026, 8, 11, 11, 0),
        },

        # Responsable RH
        {
            "candidat_email": "olfa.chaabane@example.com",
            "offre_titre": "Responsable Ressources Humaines",
            "statut": "en_attente",
            "note_evaluation": 4,
            "commentaire": "Entretien RH très concluant. Attente de la validation de la direction générale.",
            "date_rh": datetime(2026, 8, 14, 14, 0),
            "date_tech": None,
        },

        # Logistique
        {
            "candidat_email": "mohamed.triki@example.com",
            "offre_titre": "Gestionnaire Supply Chain & Logistique",
            "statut": "acceptee",
            "note_evaluation": 4,
            "commentaire": "Compétences SAP et douane vérifiées. Prise de poste programmée.",
            "date_rh": datetime(2026, 8, 12, 10, 0),
            "date_tech": datetime(2026, 8, 14, 16, 0),
        }
    ]

    for cand_app in candidatures_data:
        candidat_obj = candidats.get(cand_app["candidat_email"])
        offre_obj = offres.get(cand_app["offre_titre"])

        if candidat_obj and offre_obj:
            dt_rh = timezone.make_aware(cand_app["date_rh"]) if cand_app["date_rh"] else None
            dt_tech = timezone.make_aware(cand_app["date_tech"]) if cand_app["date_tech"] else None

            Candidature.objects.update_or_create(
                candidat=candidat_obj,
                offre=offre_obj,
                defaults={
                    "statut": cand_app["statut"],
                    "note_evaluation": cand_app["note_evaluation"],
                    "commentaire": cand_app["commentaire"],
                    "date_entretien_rh": dt_rh,
                    "date_entretien_technique": dt_tech,
                }
            )

    print("Mise à jour idempotente effectuée avec succès pour le recruteur 'simac'.")