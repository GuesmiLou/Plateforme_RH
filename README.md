# Plateforme RH

## À propos

Plateforme RH est une application web développée avec Django et PostgreSQL permettant la gestion des offres d'emploi et des candidatures. Elle offre l'ajout d'offres, le dépôt de CV, la recherche de candidats par mots-clés et le suivi des statuts de recrutement (en attente, accepté, refusé)

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Contribution](#contribution)
- [Construit avec](#construit-avec)
- [Gestion des versions](#gestion-des-versions)
- [Licence](#licence)

## Prérequis

- [Python](https://www.python.org/) 3.11 ou plus
- [PostgreSQL](https://www.postgresql.org/) 14 ou plus
- pip (fourni avec Python)

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

L'application est ensuite accessible sur `http://127.0.0.1:8000/` et l'interface d'administration sur `http://127.0.0.1:8000/admin`.

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

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/) — framework web
- [PostgreSQL](https://www.postgresql.org/) — base de données

## Gestion des versions

La dénomination des versions suit la [gestion sémantique de version](https://semver.org/lang/fr/) (MAJEUR.MINEUR.CORRECTIF).

## Licence

Projet académique réalisé dans le cadre d'un stage / d'un module universitaire (ISIMG).
