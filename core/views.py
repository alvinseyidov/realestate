import os

from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Contact, Feature, Waitlist
from offer.models import Offer
from statik.models import *
from django.http import JsonResponse


def data(request, year, amount, mortgage):
    from google.oauth2 import service_account
    import googleapiclient.discovery
    from googleapiclient.discovery import build

    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media/realestategoogle.json")

    # Define the scopes
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # Create credentials using the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the service
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    # Now you can use 'service' to interact with the Google Sheets API

    # Your spreadsheet ID and range
    spreadsheet_id = '1H01hPz3N8ojofEKw0p1gZCf13BfF-ZoDX4VzAi-zGWg'
    range_name = 'Sheet1!D2'
    range_name2 = 'Sheet1!E20'

    # Read data
    sheet = service.spreadsheets()

    values = [
        [amount],  # First row
        # Add more rows as needed
    ]

    # Prepare the request body
    body = {
        'values': values
    }

    request = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body)

    response = request.execute()

    READ_RANGES = ['Sheet1!E20', 'Sheet1!F20', 'Sheet1!G20', 'Sheet1!H20', 'Sheet1!I20', 'Sheet1!J20', 'Sheet1!K20',
                   'Sheet1!L20', 'Sheet1!L20', 'Sheet1!M20']
    READ_RANGES2 = ['Sheet1!E35', 'Sheet1!F35', 'Sheet1!G35', 'Sheet1!H35', 'Sheet1!I35', 'Sheet1!J35', 'Sheet1!K35',
                    'Sheet1!L35', 'Sheet1!L35', 'Sheet1!M35']
    READ_RANGES3 = ['Sheet1!E57', 'Sheet1!F57', 'Sheet1!G57', 'Sheet1!H57', 'Sheet1!I57', 'Sheet1!J57', 'Sheet1!K57',
                    'Sheet1!L57', 'Sheet1!L57', 'Sheet1!M57']
    READ_RANGES4 = ['Sheet1!E72', 'Sheet1!F72', 'Sheet1!G72', 'Sheet1!H72', 'Sheet1!I72', 'Sheet1!J72', 'Sheet1!K72',
                    'Sheet1!L72', 'Sheet1!L72', 'Sheet1!M72']
    READ_RANGES5 = ['Sheet1!E43', 'Sheet1!F43', 'Sheet1!G43', 'Sheet1!H43', 'Sheet1!I43', 'Sheet1!J43', 'Sheet1!K43',
                    'Sheet1!L43', 'Sheet1!L43', 'Sheet1!M43']


    data = {}
    batch_get_request = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=READ_RANGES[:int(year)])
    batch_get_response = batch_get_request.execute()
    all_values_flat = []
    for value_range in batch_get_response.get('valueRanges', []):
        for row in value_range.get('values', []):
            all_values_flat.extend(row)

    data['datatr'] = all_values_flat

    batch_get_request2 = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=READ_RANGES2[:int(year)])
    batch_get_response2 = batch_get_request2.execute()
    all_values_flat2 = []
    for value_range in batch_get_response2.get('valueRanges', []):
        for row in value_range.get('values', []):
            all_values_flat2.extend(row)

    data['dataaz'] = all_values_flat2

    batch_get_request3 = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=READ_RANGES3[:int(year)])
    batch_get_response3 = batch_get_request3.execute()
    all_values_flat3 = []
    for value_range in batch_get_response3.get('valueRanges', []):
        for row in value_range.get('values', []):
            all_values_flat3.extend(row)

    data['datatr2'] = all_values_flat3

    batch_get_request4 = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=READ_RANGES4[:int(year)])
    batch_get_response4 = batch_get_request4.execute()
    all_values_flat4 = []
    for value_range in batch_get_response4.get('valueRanges', []):
        for row in value_range.get('values', []):
            all_values_flat4.extend(row)

    data['dataaz2'] = all_values_flat4

    batch_get_request5 = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=READ_RANGES5[:int(year)])
    batch_get_response5 = batch_get_request5.execute()
    all_values_flat5 = []
    for value_range in batch_get_response5.get('valueRanges', []):
        for row in value_range.get('values', []):
            all_values_flat5.extend(row)

    data['databank'] = all_values_flat5

    # Declares and asks for user to input loan amount. Then converts to float
    loanAmount = amount
    loanAmount = float(loanAmount)

    # Declares and asks user to input number of payments in years. Then converts to float. Years * 12 to get
    #  total number of months
    years = year
    years = float(years) * 12

    # Declares and asks user to input interest rate. Then converts to float and input interest rate is /100/12
    interestRate = 7.08
    interestRate = float(interestRate) / 100 / 12

    # Formula to calculate monthly payments
    mortgagePayment = loanAmount * (interestRate * (1 + interestRate)
                                    ** years) / ((1 + interestRate) ** years - 1)

    # Prints monthly payment on next line and reformat the string to a float using 2 decimal places
    print("The monthly mortgage payment is\n (%.2f) " % mortgagePayment)

    data['field11'] = 4.889 * mortgagePayment / 100 * 12
    data['field12'] = []
    data['field21'] = []
    data['field22'] = []
    data['year'] = int(year)

    if mortgage == 1:
        if year == 2:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:F16'
        elif year == 3:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:G16'
        elif year == 4:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:H16'
        elif year == 5:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:I16'
        elif year == 6:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:J16'
        elif year == 7:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:K16'
        elif year == 8:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:L16'
        elif year == 9:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:M16'
        elif year == 10:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E16:N16'
    else:
        if year == 2:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:F53'
        elif year == 3:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:G53'
        elif year == 4:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:H53'
        elif year == 5:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:I53'
        elif year == 6:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:J53'
        elif year == 7:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:K53'
        elif year == 8:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:L53'
        elif year == 9:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:M53'
        elif year == 10:
            RANGE_TO_SUM_KIRAYE = 'Sheet1!E53:N53'
    read_request_kiraye = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=RANGE_TO_SUM_KIRAYE)

    read_response_kiraye = read_request_kiraye.execute()

    # Extract the values from the response
    values = read_response_kiraye.get('values', [])
    sum_of_values_kiraye = 0

    print(values)
    for v in values[0]:
        print(v)
        sum_of_values_kiraye = sum_of_values_kiraye + int(v)



    data['kiraye'] = sum_of_values_kiraye









    if mortgage == 1:
        if year == 2:
            RANGE_TO_SUM_DEYER = 'Sheet1!F21'
        elif year == 3:
            RANGE_TO_SUM_DEYER = 'Sheet1!G21'
        elif year == 4:
            RANGE_TO_SUM_DEYER = 'Sheet1!H21'
        elif year == 5:
            RANGE_TO_SUM_DEYER = 'Sheet1!I21'
        elif year == 6:
            RANGE_TO_SUM_DEYER = 'Sheet1!J21'
        elif year == 7:
            RANGE_TO_SUM_DEYER = 'Sheet1!K21'
        elif year == 8:
            RANGE_TO_SUM_DEYER = 'Sheet1!L21'
        elif year == 9:
            RANGE_TO_SUM_DEYER = 'Sheet1!M21'
        elif year == 10:
            RANGE_TO_SUM_DEYER = 'Sheet1!N21'
    else:
        if year == 2:
            RANGE_TO_SUM_DEYER = 'Sheet1!F58'
        elif year == 3:
            RANGE_TO_SUM_DEYER = 'Sheet1!G58'
        elif year == 4:
            RANGE_TO_SUM_DEYER = 'Sheet1!H58'
        elif year == 5:
            RANGE_TO_SUM_DEYER = 'Sheet1!I58'
        elif year == 6:
            RANGE_TO_SUM_DEYER = 'Sheet1!J58'
        elif year == 7:
            RANGE_TO_SUM_DEYER = 'Sheet1!K58'
        elif year == 8:
            RANGE_TO_SUM_DEYER = 'Sheet1!L58'
        elif year == 9:
            RANGE_TO_SUM_DEYER = 'Sheet1!M58'
        elif year == 10:
            RANGE_TO_SUM_DEYER = 'Sheet1!N58'
    read_request_deyer = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=RANGE_TO_SUM_DEYER)

    read_response_deyer = read_request_deyer.execute()
    cell_value = read_response_deyer.get('values', [])[0][0] if 'values' in read_response_deyer else 0

    data['deyer'] = cell_value

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
        "main_section": main_section,
        "why_section": why_section,
        "banner1": banner1,
        "muzakire": muzakire,
        "form_section": form_section,
        "niye": niye,
        "smart": smart,
        "suallar": suallar,
        "advantage_section": advantage_section,
        "processes_section": processes_section,
        "getconsultation_section": getconsultation_section,
        "offers_section": offers_section,
        "feedback_section": feedback_section
    }
    return render(request, "index.html", context)
