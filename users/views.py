from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import UtilisateurSignUpForm


def inscription(request):
    if request.method == "POST":
        form = UtilisateurSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/admin/")
    else:
        form = UtilisateurSignUpForm()

    return render(request, "users/inscription.html", {"form": form})


def deconnexion(request):
    logout(request)
    return redirect("connexion")