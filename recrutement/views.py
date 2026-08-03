from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import OffreEmploi, Candidat, Candidature
from .forms import OffreEmploiForm, CandidatForm, CandidatureForm

@login_required
def liste_offres(request):
    offres = OffreEmploi.objects.filter(utilisateur=request.user)
    return render(request, "recrutement/liste_offres.html", {"offres": offres})


@login_required
def detail_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id)

    if offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette offre.")

    return render(request, "recrutement/detail_offre.html", {"offre": offre})


@login_required
def creer_offre(request):
    if request.method == "POST":
        form = OffreEmploiForm(request.POST)
        if form.is_valid():
            offre = form.save(commit=False)
            offre.utilisateur = request.user
            offre.save()
            return redirect("detail_offre", id=offre.id)
    else:
        form = OffreEmploiForm()

    return render(request, "recrutement/creer_offre.html", {"form": form})


@login_required
def modifier_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id)

    if offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette offre.")

    if request.method == "POST":
        form = OffreEmploiForm(request.POST, instance=offre)
        if form.is_valid():
            form.save()
            return redirect("detail_offre", id=offre.id)
    else:
        form = OffreEmploiForm(instance=offre)

    return render(request, "recrutement/modifier_offre.html", {"form": form, "offre": offre})


@login_required
def supprimer_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id)

    if offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette offre.")

    if request.method == "POST":
        offre.delete()
        return redirect("liste_offres")

    return render(request, "recrutement/supprimer_offre.html", {"offre": offre})

@login_required
def ajouter_candidature(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)

    if offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette offre.")

    if request.method == "POST":
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            Candidature.objects.create(candidat=candidat, offre=offre)
            return redirect("liste_candidatures", offre_id=offre.id)
    else:
        form = CandidatForm()

    return render(request, "recrutement/ajouter_candidature.html", {"form": form, "offre": offre})


@login_required
def liste_candidatures(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id)

    if offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette offre.")

    candidatures = Candidature.objects.filter(offre=offre)
    return render(request, "recrutement/liste_candidatures.html", {"offre": offre, "candidatures": candidatures})


@login_required
def modifier_candidature(request, id):
    candidature = get_object_or_404(Candidature, id=id)

    if candidature.offre.utilisateur != request.user:
        return HttpResponseForbidden("Vous n'avez pas accès à cette candidature.")

    if request.method == "POST":
        form = CandidatureForm(request.POST, instance=candidature)
        if form.is_valid():
            form.save()
            return redirect("liste_candidatures", offre_id=candidature.offre.id)
    else:
        form = CandidatureForm(instance=candidature)

    return render(request, "recrutement/modifier_candidature.html", {"form": form, "candidature": candidature})