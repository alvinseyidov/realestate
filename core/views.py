from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ
from offer.models import Offer


def index(request):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    villas = Offer.objects.filter(type='V')
    apartments = Offer.objects.filter(type="A")
    faq = FAQ.objects.all()
    context = {
        "faq": faq,
        "villas": villas,
        "apartments": apartments,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials
    }
    return render(request, "index.html", context)