from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("inscription/", views.inscription, name="inscription"),
    path("connexion/", views.CustomLoginView.as_view(), name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
]