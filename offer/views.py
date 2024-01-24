from django.http import JsonResponse
from django.shortcuts import render
from core.models import General, Social, Why, Tablar, Head, Body, FAQ
from offer.models import Offer, Message
from statik.models import OffersSection, Pages


def loadfaq(request):

    offset = request.GET.get('loaded_item')
    offset_int = int(offset)
    limit = 5
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(FAQ.objects.values()[offset_int:offset_int + limit])
    data = {
        'faq': post_obj,
        'offset':offset
            }
    return JsonResponse(data=data)

def offer(request, id):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    offer = Offer.objects.get(pk=id)
    offers = Offer.objects.all()[:3]
    offers_section = OffersSection.objects.last()
    if request.user_agent.is_mobile:
        is_mobile = True
    else:
        is_mobile = False
    head = Head.objects.all()
    body = Body.objects.all()
    amount = int(int(offer.price)*60/100)

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
        pages = Pages.objects.all()
        context = {
            'pages': pages,
            'amount': amount,
            'body': body,
            'head': head,
            'is_mobile': is_mobile,
            "offers": offers,
            "offer": offer,
            "tablar": tablar,
            "general": general,
            "why": why,
            "offers_section": offers_section,
            "socials": socials
        }

        return render(request, "offersuccess.html", context)
    pages = Pages.objects.all()
    context = {
        'pages': pages,
        'amount': amount,
        'body': body,
        'head': head,
        'is_mobile': is_mobile,
        "offers": offers,
        "offer": offer,
        "tablar": tablar,
        "general": general,
        "why": why,
        "offers_section": offers_section,
        "socials": socials
    }

    return render(request, "offer.html", context)