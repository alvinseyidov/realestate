from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from core.models import *
from offer.models import *
from statik.models import *
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
import io
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
    amount = int(int(offer.price)*50/100)

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

    return render(request, "pdf_template.html", context)

def offerpdf(request, id):
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
    amount = int(int(offer.price)*50/100)


    pages = Pages.objects.all()
    images = [
        {"url": request.build_absolute_uri(i.image.url)}
        for i in offer.images.all()
    ]
    print(images)
    context = {
        'images': images,
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

    html_string = render_to_string('pdf_template.html', context)

    # Create an in-memory buffer to hold the PDF
    pdf_file = io.BytesIO()

    # Generate PDF from the rendered HTML
    HTML(string=html_string).write_pdf(pdf_file)

    # Seek to the beginning of the BytesIO buffer to read the PDF
    pdf_file.seek(0)

    # Send the PDF as an HTTP response
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="offer_details.pdf"'

    return response


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




def offers(request):
    TYPE = (
        ('V', 'Villa'),
        ('A', 'Mənzil'),
        ('E', 'Ev'),
        ('T', 'Torpaq'),
        ('Q', 'Qeyri-yaşayış'),
        ('N', 'Bina'),
    )
    # Get the filtered offers based on query parameters or default to "Bina" type
    offers = Offer.objects.all()

    # Default filter for 'Bina'
    offer_type = request.GET.get('type', 'A')  # Default is 'N' for Bina
    if offer_type:
        offers = offers.filter(type=offer_type)

    # Apply additional filters if provided
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    rooms = request.GET.get('rooms')
    beds = request.GET.get('beds')
    balcon = request.GET.get('balcon')
    wc_qty = request.GET.get('wc_qty')
    square_min = request.GET.get('square_min')
    square_max = request.GET.get('square_max')

    if price_min:
        offers = offers.filter(price__gte=price_min)
    if price_max:
        offers = offers.filter(price__lte=price_max)
    if rooms:
        offers = offers.filter(rooms=rooms)
    if balcon:
        offers = offers.filter(balcon=balcon)
    if beds:
        offers = offers.filter(bed=beds)
    if wc_qty:
        offers = offers.filter(wc_qty=wc_qty)
    if square_min:
        offers = offers.filter(square__gte=square_min)
    if square_max:
        offers = offers.filter(square__lte=square_max)
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    context = {
        "general": general,
        "why": why,
        "socials": socials,


        'offers': offers,
        'offer_type': offer_type,
        'price_min': price_min,
        'price_max': price_max,
        'rooms': rooms,
        'balcon': balcon,
        'beds': beds,
        'wc_qty': wc_qty,
        'square_min': square_min,
        'square_max': square_max,
    }

    return render(request, 'offers.html', context)
