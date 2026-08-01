from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("inscription/", views.inscription, name="inscription"),
    path("connexion/", LoginView.as_view(template_name="users/connexion.html"), name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
]