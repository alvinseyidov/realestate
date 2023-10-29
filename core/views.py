from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Contact
from offer.models import Offer
from statik.models import *


def contactform(request):
    general = General.objects.last()
    socials = Social.objects.all()


    main_section = MainSection.objects.last()




    if request.method == 'POST':
        name = ''
        surname = ''
        phone = ''
        try:
            name = request.POST.get('name')
        except:
            name = ''
        try:
            surname = request.POST.get('surname')
        except:
            surname = ''
        try:
            phone = request.POST.get('phone')
        except:
            phone = ''
        Contact.objects.create(
            name=name,
            surname=surname,
            phone=phone
        )

        context = {
            "general": general,
            "socials": socials,
            "main_section": main_section,
        }
        return render(request, "success.html", context)


def index(request):
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    villas = Offer.objects.filter(type='V')
    apartments = Offer.objects.filter(type="A")
    faq = FAQ.objects.all()
    feedback = Feedback.objects.all()

    main_section = MainSection.objects.last()
    video_section = VideoSection.objects.last()
    why_section = WhySection.objects.last()
    advantage_section = AdvantageSection.objects.last()
    processes_section = ProcessesSection.objects.last()
    getconsultation_section = GetConsultationSection.objects.last()
    offers_section = OffersSection.objects.last()
    feedback_section = FeedbackSection.objects.last()
    sorting_sections = SortingSections.objects.last()


    context = {
        "sorting_sections": sorting_sections,
        "faq": faq,
        "feedback": feedback,
        "villas": villas,
        "apartments": apartments,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials,
        "main_section" : main_section,
    "video_section" :video_section,
    "why_section" :why_section,
    "advantage_section" :advantage_section,
    "processes_section" :processes_section,
    "getconsultation_section" :getconsultation_section,
    "offers_section" :offers_section,
    "feedback_section" :feedback_section
    }
    return render(request, "index.html", context)