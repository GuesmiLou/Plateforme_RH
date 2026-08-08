from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


class CustomUserModelTests(TestCase):
    """Tests unitaires pour le modèle utilisateur personnalisé (Utilisateur)."""

    def test_create_user_successful(self):
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="securepassword123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("securepassword123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_successful(self):
        superuser = User.objects.create_superuser(
            username="adminuser",
            email="admin@example.com",
            password="adminpassword123"
        )
        self.assertEqual(superuser.username, "adminuser")
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_duplicate_email_raises_integrity_error(self):
        """Vérifie l'unicité stricte de l'adresse email."""
        User.objects.create_user(
            username="user1",
            email="duplicate@example.com",
            password="password123"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="user2",
                email="duplicate@example.com",
                password="password123"
            )

    def test_str_representation(self):
        user = User.objects.create_user(
            username="rh_manager",
            email="rh@example.com",
            password="password123"
        )
        self.assertIn("rh_manager", str(user))


class UserAuthenticationTests(TestCase):
    """Tests du système de session et d'authentification."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testrh",
            email="testrh@example.com",
            password="Password123!"
        )

    def test_client_login_and_logout_session(self):
        """Vérifie l'ouverture et la fermeture de session utilisateur."""
        logged_in = self.client.login(username="testrh", password="Password123!")
        self.assertTrue(logged_in)
        self.assertIn("_auth_user_id", self.client.session)

        self.client.logout()
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_invalid_login_fails(self):
        """Vérifie le rejet des identifiants incorrects."""
        logged_in = self.client.login(username="testrh", password="WrongPassword")
        self.assertFalse(logged_in)
        self.assertNotIn("_auth_user_id", self.client.session)