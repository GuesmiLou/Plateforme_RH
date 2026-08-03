from django.urls import path
from . import views

urlpatterns = [
    path("offres/", views.liste_offres, name="liste_offres"),
    path("offres/<int:id>/", views.detail_offre, name="detail_offre"),
    path("offres/nouvelle/", views.creer_offre, name="creer_offre"),
    path("offres/<int:id>/modifier/", views.modifier_offre, name="modifier_offre"),
    path("offres/<int:id>/supprimer/", views.supprimer_offre, name="supprimer_offre"),
    path("offres/<int:offre_id>/candidatures/nouvelle/", views.ajouter_candidature, name="ajouter_candidature"),
    path("offres/<int:offre_id>/candidatures/", views.liste_candidatures, name="liste_candidatures"),
    path("candidatures/<int:id>/modifier/", views.modifier_candidature, name="modifier_candidature"),
]