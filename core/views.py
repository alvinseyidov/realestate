import os

from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Contact, Feature, Waitlist
from offer.models import Offer
from statik.models import *
from django.http import JsonResponse

def data(request, year, amount, mortgage):
    from openpyxl import load_workbook
    
    workbook = load_workbook(filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx"))
    sheet = workbook.active
    sheet["D2"] = int(amount)
    sheet["D6"] = int(year)

    # save the file
    workbook.save(filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx"))
    workbook.close()

    import xlwings as xw
    wbxl=xw.Book(os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx"))
    print(wbxl.sheets['Sheet1'].range('E20').value)
   

     

     


    data = {}

    data['datatr'] = [
        int(str(abs(wbxl.sheets['Sheet1'].range('E20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('F20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('G20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('H20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('I20').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('J20').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('K20').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('L20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('M20').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('N20').value)).split('.')[0])]

    data['dataaz'] = [
        int(str(abs(wbxl.sheets['Sheet1'].range('E35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('F35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('G35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('H35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('I35').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('J35').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('K35').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('L35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('M35').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('N35').value)).split('.')[0])]

    data['databank'] = [
        int(str(abs(wbxl.sheets['Sheet1'].range('E43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('F43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('G43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('H43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('I43').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('J43').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('K43').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('L43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('M43').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('N43').value)).split('.')[0])]


    data['datatr2'] = [
       int(str(abs(wbxl.sheets['Sheet1'].range('E57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('F57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('G57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('H57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('I57').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('J57').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('K57').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('L57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('M57').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('N57').value)).split('.')[0])]

    data['dataaz2'] = [
        int(str(abs(wbxl.sheets['Sheet1'].range('E72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('F72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('G72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('H72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('I72').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('J72').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('K72').value)).split('.')[0]),
        int(str(abs(wbxl.sheets['Sheet1'].range('L72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('M72').value)).split('.')[0]), 
        int(str(abs(wbxl.sheets['Sheet1'].range('N72').value)).split('.')[0])]

    data['field11'] =round(float(wbxl.sheets['Sheet1'].range('E20').value) * float(wbxl.sheets['Sheet1'].range('E20').value),2)
    data['field12'] =round(float(wbxl.sheets['Sheet1'].range('E20').value) * float(wbxl.sheets['Sheet1'].range('E20').value),2)

    data['field21'] =round(float(wbxl.sheets['Sheet1'].range('E20').value) * float(wbxl.sheets['Sheet1'].range('E20').value),2)
    data['field22'] =round(float(wbxl.sheets['Sheet1'].range('E20').value) * float(wbxl.sheets['Sheet1'].range('E20').value),2)

    
    wbxl.save()
    wbxl.close()
        


    return JsonResponse(data)
    


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