from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import OffreEmploi, Candidat, Candidature
from .forms import OffreEmploiForm, CandidatForm

User = get_user_model()


class RecrutementModelTests(TestCase):
    """Tests unitaires pour les modèles et méthodes __str__."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password123"
        )
        self.offre = OffreEmploi.objects.create(
            titre="Développeur Python",
            description="Poste Django",
            lieu="Paris",
            departement="IT",
            utilisateur=self.user,
        )
        self.candidat = Candidat.objects.create(
            nom="Dupont",
            prenom="Jean",
            email="jean.dupont@example.com",
            utilisateur=self.user,
        )
        self.candidature = Candidature.objects.create(
            candidat=self.candidat,
            offre=self.offre,
            statut="NOUVEAU",
        )

    def test_offre_creation_and_str(self):
        self.assertEqual(str(self.offre), "Développeur Python")
        self.assertEqual(self.offre.utilisateur, self.user)

    def test_candidat_creation_and_str(self):
        self.assertEqual(str(self.candidat), "Jean Dupont")
        self.assertEqual(self.candidat.email, "jean.dupont@example.com")

    def test_candidature_creation_and_str(self):
        self.assertIn("Jean Dupont", str(self.candidature))
        self.assertIn("Développeur Python", str(self.candidature))


class RecrutementFormTests(TestCase):
    """Tests unitaires pour la validation des formulaires."""

    def test_candidat_form_invalid_email(self):
        form_data = {"nom": "Durand", "prenom": "Marie", "email": "invalid-email"}
        form = CandidatForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class RecrutementSecurityAndIsolationTests(TestCase):
    """Tests d'accès et d'isolation des données entre utilisateurs."""

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="user1", email="user1@example.com", password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2", email="user2@example.com", password="password123"
        )

        self.offre_user1 = OffreEmploi.objects.create(
            titre="Offre User 1", description="Desc", lieu="Paris", utilisateur=self.user1
        )
        self.candidat_user1 = Candidat.objects.create(
            nom="Martin", prenom="Paul", email="paul@test.com", utilisateur=self.user1
        )

    def test_unauthenticated_redirects(self):
        """Vérifie la redirection vers la connexion pour les utilisateurs anonymes."""
        urls = [
            reverse("liste_offres"),
            reverse("creer_offre"),
            reverse("liste_candidats"),
            reverse("ajouter_candidat"),
            reverse("detail_offre", args=[self.offre_user1.id]),
            reverse("detail_candidat", args=[self.candidat_user1.id]),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 200)

    def test_data_isolation_liste_offres(self):
        """User2 ne doit pas voir les offres créées par User1."""
        self.client.login(username="user2", password="password123")
        response = self.client.get(reverse("liste_offres"))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.offre_user1, response.context["offres"])

    def test_data_isolation_detail_candidat_404(self):
        """User2 ne peut pas accéder au détail du candidat de User1."""
        self.client.login(username="user2", password="password123")
        response = self.client.get(reverse("detail_candidat", args=[self.candidat_user1.id]))
        self.assertEqual(response.status_code, 404)

    def test_data_isolation_supprimer_candidat_404(self):
        """User2 ne peut pas supprimer un candidat appartenant à User1."""
        self.client.login(username="user2", password="password123")
        response = self.client.post(reverse("supprimer_candidat", args=[self.candidat_user1.id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Candidat.objects.filter(id=self.candidat_user1.id).exists())


class RecrutementCRUDAndFilterTests(TestCase):
    """Tests d'intégration des parcours d'utilisation (recherche et suppression)."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="rh_admin", email="rh_admin@example.com", password="password123"
        )
        self.client.login(username="rh_admin", password="password123")

        self.offre = OffreEmploi.objects.create(
            titre="Développeur Fullstack",
            description="React et Django",
            lieu="Nantes",
            departement="IT",
            utilisateur=self.user,
        )
        self.candidat = Candidat.objects.create(
            nom="Bonnard",
            prenom="Luc",
            email="luc.bonnard@example.com",
            competences="Python, Django, SQL",
            utilisateur=self.user,
        )

    def test_supprimer_offre_view(self):
        url = reverse("supprimer_offre", args=[self.offre.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(OffreEmploi.objects.filter(id=self.offre.id).exists())

    def test_supprimer_candidat_view(self):
        url = reverse("supprimer_candidat", args=[self.candidat.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Candidat.objects.filter(id=self.candidat.id).exists())

    def test_recherche_cvtheque_filter(self):
        response = self.client.get(reverse("liste_candidats") + "?q=Python")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.candidat, response.context["candidats"])

        response_empty = self.client.get(reverse("liste_candidats") + "?q=MotInexistant")
        self.assertEqual(response_empty.status_code, 200)
        self.assertNotIn(self.candidat, response_empty.context["candidats"])