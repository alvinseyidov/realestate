import os

from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Contact, Feature, Waitlist
from offer.models import Offer
from statik.models import *
from django.http import JsonResponse

def data(request, year, amount, mortgage):
    from openpyxl import load_workbook
    import pythoncom
    workbook = load_workbook(filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx"))
    sheet = workbook.active
    sheet["D2"] = int(amount)
    sheet["D6"] = int(year)

    # save the file
    workbook.save(filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx"))
    workbook.close()

    
    import win32com.client
    Excel = win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())

    file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/yield.xlsx")
    wb = Excel.Workbooks.Open(file)
    sheet = wb.ActiveSheet
    try:
        print("valueeeeeeeeeeeeeee")
        boo = sheet.Cells(3, 4).value
        print(sheet.Cells(20, 5).value)
        data = {}
        
        data['datatr'] = [
        int(str(abs(sheet.Cells(20, 5).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 6).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 7).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 8).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 9).value)).split('.')[0]),
        int(str(abs(sheet.Cells(20, 10).value)).split('.')[0]),
        int(str(abs(sheet.Cells(20, 11).value)).split('.')[0]),
        int(str(abs(sheet.Cells(20, 12).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 13).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(20, 14).value)).split('.')[0])]

        data['dataaz'] = [
        int(str(abs(sheet.Cells(35, 5).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 6).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 7).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 8).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 9).value)).split('.')[0]),
        int(str(abs(sheet.Cells(35, 10).value)).split('.')[0]),
        int(str(abs(sheet.Cells(35, 11).value)).split('.')[0]),
        int(str(abs(sheet.Cells(35, 12).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 13).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(35, 14).value)).split('.')[0])]

        data['databank'] = [
        int(str(abs(sheet.Cells(43, 5).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 6).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 7).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 8).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 9).value)).split('.')[0]),
        int(str(abs(sheet.Cells(43, 10).value)).split('.')[0]),
        int(str(abs(sheet.Cells(43, 11).value)).split('.')[0]),
        int(str(abs(sheet.Cells(43, 12).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 13).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(43, 14).value)).split('.')[0])]


        data['datatr2'] = [
        int(str(abs(sheet.Cells(57, 5).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 6).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 7).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 8).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 9).value)).split('.')[0]),
        int(str(abs(sheet.Cells(57, 10).value)).split('.')[0]),
        int(str(abs(sheet.Cells(57, 11).value)).split('.')[0]),
        int(str(abs(sheet.Cells(57, 12).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 13).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(57, 14).value)).split('.')[0])]

        data['dataaz2'] = [
        int(str(abs(sheet.Cells(72, 5).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 6).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 7).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 8).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 9).value)).split('.')[0]),
        int(str(abs(sheet.Cells(72, 10).value)).split('.')[0]),
        int(str(abs(sheet.Cells(72, 11).value)).split('.')[0]),
        int(str(abs(sheet.Cells(72, 12).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 13).value)).split('.')[0]), 
        int(str(abs(sheet.Cells(72, 14).value)).split('.')[0])]

        data['field11'] =round(float(sheet.Cells(7, 4).value) * float(sheet.Cells(7, 4).value),2)
        data['field12'] =round(float(sheet.Cells(7, 4).value) * float(sheet.Cells(4, 4).value),2)

        data['field21'] =round(float(sheet.Cells(74, 9).value) * float(sheet.Cells(7, 4).value),2)
        data['field22'] =round(float(sheet.Cells(75, 9).value) * float(sheet.Cells(4, 4).value),2)
        wb.Close(True)
    except:
        wb.Close(True)
    
        


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