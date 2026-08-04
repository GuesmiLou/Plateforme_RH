# Plateforme RH

## À propos

Plateforme RH est une application web développée avec Django et PostgreSQL permettant la gestion des offres d'emploi et des candidatures. Elle offre l'ajout d'offres, le dépôt de CV, la recherche de candidats par mots-clés et le suivi des statuts de recrutement (en attente, accepté, refusé)

## Table des matières

* [Prérequis](https://www.google.com/search?q=%23pr%C3%A9requis)
* [Installation](https://www.google.com/search?q=%23installation)
* [Utilisation](https://www.google.com/search?q=%23utilisation)
* [Routes de l'application](https://www.google.com/search?q=%23routes-de-lapplication)
* [Structure du projet](https://www.google.com/search?q=%23structure-du-projet)
* [Contribution](https://www.google.com/search?q=%23contribution)
* [Construit avec](https://www.google.com/search?q=%23construit-avec)
* [Gestion des versions](https://www.google.com/search?q=%23gestion-des-versions)
* [Licence](https://www.google.com/search?q=%23licence)

## Prérequis

* [Python](https://www.python.org/) 3.11 ou plus
* [PostgreSQL](https://www.postgresql.org/) 14 ou plus
* pip (fourni avec Python)

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/GuesmiLou/Plateforme_RH.git
cd Plateforme_RH

# 2. Créer et activer un environnement virtuel
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Créer la base de données PostgreSQL
#    (dans psql ou pgAdmin)
#    CREATE DATABASE plateforme_rh_db;

# 5. Copier le fichier d'exemple des variables d'environnement
#    et renseigner ses propres valeurs (voir .env.example)
copy .env.example .env      # Windows
# cp .env.example .env       # macOS / Linux

# 6. Appliquer les migrations
python manage.py migrate

# 7. Créer un super-utilisateur
python manage.py createsuperuser

```

## Utilisation

```bash
# Lancer le serveur de développement
python manage.py runserver

```

L'application est ensuite accessible sur `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)` et l'interface d'administration sur `[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)`.

## Routes de l'application

### Authentification & Accueil

| Route | Nom de l'URL | Accès | Description |
| --- | --- | --- | --- |
| `/` | `accueil` | Public | Page d'accueil (redirection automatique selon le rôle si connecté) |
| `/connexion/` | `connexion` | Public | Formulaire de connexion pour recruteurs et administrateurs |
| `/inscription/` | `inscription` | Public | Formulaire de création de compte entreprise recruteur |
| `/deconnexion/` | `deconnexion` | Authentifié | Déconnexion de la session utilisateur |

### Espace Recrutement (`/recrutement/`)

| Route | Nom de l'URL | Accès | Description |
| --- | --- | --- | --- |
| `/recrutement/` | `liste_offres` | Recruteur | Dashboard des offres d'emploi avec filtres de recherche |
| `/recrutement/creer/` | `creer_offre` | Recruteur | Formulaire de création d'une nouvelle offre d'emploi |
| `/recrutement/<id>/` | `detail_offre` | Recruteur | Consultation détaillée d'une offre d'emploi |
| `/recrutement/<id>/modifier/` | `modifier_offre` | Recruteur | Formulaire de modification d'une offre d'emploi |
| `/recrutement/<id>/supprimer/` | `supprimer_offre` | Recruteur | Confirmation de suppression d'une offre |
| `/recrutement/<offre_id>/candidatures/` | `liste_candidatures` | Recruteur | Suivi et filtrage des candidatures associées à une offre |
| `/recrutement/<offre_id>/candidatures/ajouter/` | `ajouter_candidature` | Recruteur | Ajout d'un candidat et dépôt de sa candidature |
| `/recrutement/candidatures/<id>/modifier/` | `modifier_candidature` | Recruteur | Évaluation et mise à jour du statut d'une candidature |

### Administration

| Route | Nom de l'URL | Accès | Description |
| --- | --- | --- | --- |
| `/admin/` | `admin:index` | Admin / Staff | Panneau de gestion globale de la plateforme Django |

## Structure du projet

```
Plateforme_RH/
├── users/          # Authentification, profils Candidat et Recruteur
├── recrutement/    # Offres d'emploi et candidatures
├── manage.py
├── requirements.txt
└── README.md

```

Chaque nouvelle fonctionnalité majeure peut être ajoutée comme une nouvelle app Django (ex: `notifications/`), en suivant la même structure que `users/` et `recrutement/`.

## Contribution

```bash
# Créer une branche pour une nouvelle fonctionnalité
git checkout -b feature/nom-de-la-fonctionnalite

# Après les modifications
git add .
git commit -m "Description claire du changement"
git push origin feature/nom-de-la-fonctionnalite

```

## Construit avec

### Langages & Frameworks

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) — framework web
* [PostgreSQL](https://www.postgresql.org/) — base de données

## Gestion des versions

La dénomination des versions suit la [gestion sémantique de version](https://semver.org/lang/fr/) (MAJEUR.MINEUR.CORRECTIF).

## Licence

Projet académique réalisé dans le cadre d'un stage / d'un module universitaire (ISIMG).
