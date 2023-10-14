from django.shortcuts import render
from core.models import General, Social, Why, Tablar
from offer.models import Offer


def index(request):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    offers = Offer.objects.all()
    context = {
        "offers": offers,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials
    }
    return render(request, "index.html", context)