from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import UtilisateurSignUpForm


def inscription(request):
    if request.method == "POST":
        form = UtilisateurSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False  
            user.save()
            return redirect("connexion")
    else:
        form = UtilisateurSignUpForm()

    return render(request, "users/inscription.html", {"form": form})


def deconnexion(request):
    logout(request)
    return redirect("connexion")

def accueil(request):
    return render(request, "users/accueil.html")


class CustomLoginView(LoginView):
    template_name = "users/connexion.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return "/admin/"
        return "/recrutement/offres/"