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

    return render(request, "offer.html", context)

from django.templatetags.static import static
from django.utils.html import mark_safe

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
    image_url1 = request.build_absolute_uri(static('1.svg'))
    image_urlstairs = request.build_absolute_uri(static('stairs.png'))
    image_url4 = request.build_absolute_uri(static('4.svg'))
    image_url5 = request.build_absolute_uri(static('5.svg'))
    image_url6 = request.build_absolute_uri(static('6.svg'))
    image_url7 = request.build_absolute_uri(static('7.svg'))
    image_url8 = request.build_absolute_uri(static('8.svg'))
    image_url9 = request.build_absolute_uri(static('9.svg'))
    image_url10 = request.build_absolute_uri(static('10.svg'))
    image_url11 = request.build_absolute_uri(static('11.svg'))
    image_url12 = request.build_absolute_uri(static('12.svg'))
    image_urls = [request.build_absolute_uri(image.image.url) for image in offer.images.all()]
    context = {
        'image_urls': image_urls,
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
        "socials": socials,
        "image_url1": image_url1,
        "image_url4": image_url4,
        "image_url5": image_url5,
        "image_url6": image_url6,
        "image_url7": image_url7,
        "image_url8": image_url8,
        "image_url9": image_url9,
        "image_url10": image_url10,
        "image_url11": image_url11,
        "image_url12": image_url12,
        "image_urlstairs": image_urlstairs,

    }

    html_string = render_to_string('pdf_template.html', context)

    # Create a BytesIO buffer to hold the PDF data
    pdf_file = io.BytesIO()

    # Generate the PDF from the HTML string and write it to the buffer
    html = HTML(string=html_string)
    html.write_pdf(target=pdf_file)  # Use `target=pdf_file` explicitly

    # Move to the start of the buffer
    pdf_file.seek(0)

    # Create an HTTP response with the PDF content
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
    # Retrieve filter values from the request or set defaults
    location_id = request.GET.get('location', 'all')
    property_type = request.GET.get('property_type', 'all')
    room_qty = request.GET.get('room_qty', 'all')
    extra_area = request.GET.get('extra_area', 'all')
    installment = request.GET.get('installment', 'all')
    suitable_for_citizenship = request.GET.get('suitable_for_citizenship', 'all')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_square = request.GET.get('min_square')

    # Start with all offers
    offers = Offer.objects.all()

    # Apply filters if they’re not set to "all"
    if location_id != 'all':
        offers = offers.filter(location_id=location_id)

    if property_type != 'all':
        offers = offers.filter(type=property_type)

    if room_qty != 'all':
        if room_qty == 'more':
            offers = offers.exclude(bed__in=['1+1', '2+1', '3+1'])
        else:
            offers = offers.filter(bed=room_qty)

    if extra_area != 'all':
        offers = offers.filter(elave_sahe=extra_area)

    if installment != 'all':
        if installment == 'var':
            offers = offers.filter(installment='var')
        else:
            offers = offers.exclude(installment='var')

    if suitable_for_citizenship != 'all':
        if suitable_for_citizenship == 'var':
            offers = offers.filter(suitable_for_citizenship='var')
        else:
            offers = offers.exclude(suitable_for_citizenship='var')

    if min_price:
        offers = offers.filter(price__gte=min_price)
    if max_price:
        offers = offers.filter(price__lte=max_price)

        # Apply square footage filters (assuming square is stored as an integer in a CharField)
    if min_square:
        offers = offers.filter(square__gte=int(min_square))

    locations = Location.objects.all()
    if location_id != 'all':
        location_id = int(location_id)
    # Pass filter selections to the template to retain selections on reload

    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    context = {
        "general": general,
        "why": why,
        "socials": socials,


        'offers': offers,
        'locations': locations,
        'selected_location': location_id,
        'selected_property_type': property_type,
        'selected_room_qty': room_qty,
        'selected_extra_area': extra_area,
        'selected_installment': installment,
        'selected_suitable_for_citizenship': suitable_for_citizenship,
        'min_price': min_price,
        'max_price': max_price,
        'min_square': min_square,
    }

    return render(request, 'offers.html', context)
