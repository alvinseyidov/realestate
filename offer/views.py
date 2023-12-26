from django.shortcuts import render
from core.models import General, Social, Why, Tablar, Head, Body
from offer.models import Offer, Message


def offer(request, id):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    offer = Offer.objects.get(pk=id)
    offers = Offer.objects.all()
    if request.user_agent.is_mobile:
        is_mobile = True
    else:
        is_mobile = False
    head = Head.objects.all()
    body = Body.objects.all()

    if request.method == 'POST':
        first_name = ''
        last_name = ''
        phone = ''
        email = ''
        message = ''
        try:
            first_name = request.POST.get('first_name')
        except:
            first_name = ''
        try:
            last_name = request.POST.get('last_name')
        except:
            last_name = ''
        try:
            phone = request.POST.get('phone')
        except:
            phone = ''

        try:
            email = request.POST.get('email')
        except:
            email = ''

        try:
            message = request.POST.get('message')
        except:
            message = ''

        Message.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
            phone=phone
        )
        context = {
            'body': body,
            'head': head,
            'is_mobile': is_mobile,
            "offers": offers,
            "offer": offer,
            "tablar": tablar,
            "general": general,
            "why": why,
            "socials": socials
        }

        return render(request, "offersuccess.html", context)
    context = {
        'body': body,
        'head': head,
        'is_mobile': is_mobile,
        "offers": offers,
        "offer": offer,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials
    }

    return render(request, "offer.html", context)