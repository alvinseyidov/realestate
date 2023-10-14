from django.shortcuts import render
from core.models import General, Social, Why, Tablar
from offer.models import Offer


def offer(request, id):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    offer = Offer.objects.get(pk=id)
    offers = Offer.objects.all()
    context = {
        "offers": offers,
        "offer": offer,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials
    }

    return render(request, "offer.html", context)