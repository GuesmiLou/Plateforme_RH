from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import OffreEmploi, Candidat, Candidature
from .forms import OffreEmploiForm, CandidatForm, CandidatureForm


#OFFRES D'EMPLOI

@login_required
@require_http_methods(["GET"])
def liste_offres(request):
    offres = OffreEmploi.objects.filter(utilisateur=request.user)
    q = request.GET.get('q', '').strip()
    statut = request.GET.get('statut', '').strip()
    type_contrat = request.GET.get('type_contrat', '').strip()
    mode_travail = request.GET.get('mode_travail', '').strip()

    if q:
        offres = offres.filter(
            Q(titre__icontains=q) | 
            Q(description__icontains=q) | 
            Q(lieu__icontains=q) |
            Q(departement__icontains=q)
        )
    if statut:
        offres = offres.filter(statut_offre=statut)
    if type_contrat:
        offres = offres.filter(type_contrat=type_contrat)
    if mode_travail:
        offres = offres.filter(mode_travail=mode_travail)

    context = {
        "offres": offres,
        "q": q,
        "statut": statut,
        "type_contrat": type_contrat,
        "mode_travail": mode_travail,
        "type_contrat_choices": OffreEmploi.TypeContrat.choices,
        "mode_travail_choices": OffreEmploi.ModeTravail.choices,
    }
    return render(request, "recrutement/liste_offres.html", context)


@login_required
@require_http_methods(["GET"])
def detail_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id, utilisateur=request.user)
    return render(request, "recrutement/detail_offre.html", {"offre": offre})


@login_required
@require_http_methods(["GET", "POST"])
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
@require_http_methods(["GET", "POST"])
def modifier_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id, utilisateur=request.user)

    if request.method == "POST":
        form = OffreEmploiForm(request.POST, instance=offre)
        if form.is_valid():
            form.save()
            return redirect("detail_offre", id=offre.id)
    else:
        form = OffreEmploiForm(instance=offre)

    return render(request, "recrutement/modifier_offre.html", {"form": form, "offre": offre})


@login_required
@require_http_methods(["GET", "POST"])
def supprimer_offre(request, id):
    offre = get_object_or_404(OffreEmploi, id=id, utilisateur=request.user)

    if request.method == "POST":
        offre.delete()
        return redirect("liste_offres")

    return render(request, "recrutement/supprimer_offre.html", {"offre": offre})


#CVTHÈQUE / CANDIDATS

@login_required
@require_http_methods(["GET"])
def liste_candidats(request):
    candidats = Candidat.objects.filter(utilisateur=request.user)
    q = request.GET.get('q', '').strip()

    if q:
        candidats = candidats.filter(
            Q(nom__icontains=q) |
            Q(prenom__icontains=q) |
            Q(email__icontains=q) |
            Q(competences__icontains=q)
        )

    return render(request, "recrutement/liste_candidats.html", {
        "candidats": candidats,
        "q": q,
    })


@login_required
@require_http_methods(["GET", "POST"])
def ajouter_candidat(request):
    if request.method == "POST":
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save(commit=False)
            candidat.utilisateur = request.user
            candidat.save()
            return redirect("liste_candidats")
    else:
        form = CandidatForm()

    return render(request, "recrutement/form_candidat.html", {"form": form, "titre": "Ajouter un candidat"})


@login_required
@require_http_methods(["GET"])
def detail_candidat(request, id):
    candidat = get_object_or_404(Candidat, id=id, utilisateur=request.user)
    candidatures = Candidature.objects.filter(candidat=candidat)
    return render(request, "recrutement/detail_candidat.html", {
        "candidat": candidat,
        "candidatures": candidatures,
    })



@login_required
@require_http_methods(["GET", "POST"])
def supprimer_candidat(request, id):
    candidat = get_object_or_404(Candidat, id=id, utilisateur=request.user)

    if request.method == "POST":
        candidat.delete()
        return redirect("liste_candidats")

    return render(request, "recrutement/supprimer_candidat.html", {"candidat": candidat})


# --- CANDIDATURES ---

@login_required
@require_http_methods(["GET", "POST"])
def ajouter_candidature(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id, utilisateur=request.user)

    if request.method == "POST":
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save(commit=False)
            candidat.utilisateur = request.user
            candidat.save()
            Candidature.objects.create(candidat=candidat, offre=offre)
            return redirect("liste_candidatures", offre_id=offre.id)
    else:
        form = CandidatForm()

    return render(request, "recrutement/ajouter_candidature.html", {"form": form, "offre": offre})


@login_required
@require_http_methods(["GET"])
def liste_candidatures(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id, utilisateur=request.user)
    candidatures = Candidature.objects.filter(offre=offre)

    q = request.GET.get('q', '').strip()
    statut = request.GET.get('statut', '').strip()
    note = request.GET.get('note', '').strip()

    if q:
        candidatures = candidatures.filter(
            Q(candidat__nom__icontains=q) |
            Q(candidat__prenom__icontains=q) |
            Q(candidat__email__icontains=q) |
            Q(candidat__competences__icontains=q)
        )
    if statut:
        candidatures = candidatures.filter(statut=statut)
    if note.isdigit():
        candidatures = candidatures.filter(note_evaluation=int(note))

    context = {
        "offre": offre,
        "candidatures": candidatures,
        "q": q,
        "statut": statut,
        "note": note,
    }
    return render(request, "recrutement/liste_candidatures.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def modifier_candidature(request, id):
    candidature = get_object_or_404(Candidature, id=id, offre__utilisateur=request.user)
    if request.method == "POST":
        form = CandidatureForm(request.POST, instance=candidature)
        if form.is_valid():
            form.save()
            return redirect("liste_candidatures", offre_id=candidature.offre.id)
    else:
        form = CandidatureForm(instance=candidature)

    return render(request, "recrutement/modifier_candidature.html", {"form": form, "candidature": candidature})

@login_required
@require_http_methods(["GET", "POST"])
def assigner_candidat_existant(request, offre_id):
    offre = get_object_or_404(OffreEmploi, id=offre_id, utilisateur=request.user)
    candidats_disponibles = Candidat.objects.filter(
        utilisateur=request.user
    ).exclude(candidature__offre=offre)

    if request.method == "POST":
        candidat_id = request.POST.get("candidat_id")
        if candidat_id:
            candidat = get_object_or_404(Candidat, id=candidat_id, utilisateur=request.user)
            Candidature.objects.create(candidat=candidat, offre=offre)
            return redirect("liste_candidatures", offre_id=offre.id)

    return render(
        request, 
        "recrutement/assigner_candidat.html", 
        {"offre": offre, "candidats": candidats_disponibles}
    )