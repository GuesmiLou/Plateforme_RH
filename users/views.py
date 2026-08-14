from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from .forms import UtilisateurSignUpForm


def inscription(request):
    if request.user.is_authenticated:
        return redirect("liste_offres")

    if request.method == "POST":
        form = UtilisateurSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False  
            user.save()
            messages.success(request, "Compte créé avec succès ! Vous pouvez vous connecter.")
            return redirect("connexion")
    else:
        form = UtilisateurSignUpForm()

    return render(request, "users/inscription.html", {"form": form})


@require_POST
def deconnexion(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect("connexion")


def accueil(request):
    return render(request, "users/accueil.html")


class CustomLoginView(LoginView):
    template_name = "users/connexion.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return reverse("admin:index")
        return reverse("liste_offres")