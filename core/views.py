from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Contact, Feature, Waitlist
from offer.models import Offer
from statik.models import *



def contactform2(request):
    general = General.objects.last()
    socials = Social.objects.all()


    main_section = MainSection.objects.last()




    if request.method == 'POST':
        email = ''

        try:
            email = request.POST.get('email')
        except:
            email = ''

        Waitlist.objects.create(
            email=email,
        )

        context = {
            "general": general,
            "socials": socials,
            "main_section": main_section,
        }
        return render(request, "success2.html", context)


def contactform(request):
    general = General.objects.last()
    socials = Social.objects.all()


    main_section = MainSection.objects.last()




    if request.method == 'POST':
        name = ''
        email = ''
        phone = ''
        try:
            name = request.POST.get('name')
        except:
            name = ''
        try:
            email = request.POST.get('email')
        except:
            email = ''
        try:
            phone = request.POST.get('phone')
        except:
            phone = ''
        Contact.objects.create(
            name=name,
            email=email,
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

    features = Feature.objects.all()
    main_section = MainSection.objects.last()
    why_section = WhySection.objects.last()
    advantage_section = AdvantageSection.objects.last()
    processes_section = ProcessesSection.objects.last()
    getconsultation_section = GetConsultationSection.objects.last()
    offers_section = OffersSection.objects.last()
    form_section = FormSection.objects.last()
    feedback_section = FeedbackSection.objects.last()
    muzakire = MuzakireEdek.objects.last()
    sorting_sections = SortingSections.objects.last()
    banner1 = GeliriHesablaBanner.objects.last()
    smart = SmartInvest.objects.last()
    niye = NiyeSecirler.objects.last()
    suallar = Suallar.objects.all()


    context = {
        "sorting_sections": sorting_sections,
        "features": features,
        "faq": faq,
        "feedback": feedback,
        "villas": villas,
        "apartments": apartments,
        "tablar": tablar,
        "general": general,
        "why": why,
        "socials": socials,
        "main_section" : main_section,
    "why_section" :why_section,
    "banner1" :banner1,
    "muzakire" :muzakire,
    "form_section" :form_section,
    "niye" :niye,
    "smart" :smart,
    "suallar" :suallar,
    "advantage_section" :advantage_section,
    "processes_section" :processes_section,
    "getconsultation_section" :getconsultation_section,
    "offers_section" :offers_section,
    "feedback_section" :feedback_section
    }
    return render(request, "index.html", context)