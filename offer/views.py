from django.http import JsonResponse
from django.shortcuts import render
from core.models import *
from offer.models import *
from statik.models import *


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
    form_menzil_form = MenzilForm.objects.all()
    form1 = Form1.objects.last()
    form2 = Form2.objects.last()
    form3 = Form3.objects.last()
    form4 = Form4.objects.last()
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
            'form_menzil_form': form_menzil_form,
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
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
        'form_menzil_form': form_menzil_form,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
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

def offertr(request, id):
    form1 = Form1TR.objects.last()
    form2 = Form2TR.objects.last()
    form3 = Form3TR.objects.last()
    form4 = Form4TR.objects.last()
    general = GeneralTR.objects.last()
    socials = Social.objects.all()
    why = WhyTR.objects.all()
    tablar = Tablar.objects.all()
    offer = OfferTR.objects.get(pk=id)
    offers = OfferTR.objects.all()[:3]
    offers_section = OffersSectionTR.objects.last()
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
        pages = PagesTR.objects.all()
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
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
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
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

    return render(request, "offertr.html", context)

def offerru(request, id):
    form1 = Form1RU.objects.last()
    form2 = Form2RU.objects.last()
    form3 = Form3RU.objects.last()
    form4 = Form4RU.objects.last()
    general = GeneralRU.objects.last()
    socials = Social.objects.all()
    why = WhyRU.objects.all()
    tablar = Tablar.objects.all()
    offer = OfferRU.objects.get(pk=id)
    offers = OfferRU.objects.all()[:3]
    offers_section = OffersSectionRU.objects.last()
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
        pages = PagesRU.objects.all()
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
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
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
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

    return render(request, "offerru.html", context)

def tr(request):
    from django_user_agents.utils import get_user_agent
    user_agent = get_user_agent(request)

    slider = SliderTR.objects.all()
    feedback = FeedbackTR.objects.all()
    context = {
        "slider": slider,
        "feedback": feedback

    }
    if user_agent.is_mobile:
        return render(request, "trm.html", context)
    else:
        return render(request, "tr.html", context)
