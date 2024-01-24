import os

from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Feature, Head, Body, Parametr, Slider, \
    CalendlyScript
from contact.models import Contact, Waitlist
from offer.models import Offer
from statik.models import *
from django.http import JsonResponse

def calculate_mortgage(loanAmount,years, interestRate):
    loanAmount = float(loanAmount)

    # Declares and asks user to input number of payments in years. Then converts to float. Years * 12 to get
    #  total number of months
    years = float(years) * 12

    # Declares and asks user to input interest rate. Then converts to float and input interest rate is /100/12
    interestRate = float(interestRate) / 100 / 12

    # Formula to calculate monthly payments
    mortgagePayment = loanAmount * (interestRate * (1 + interestRate)
                                    ** years) / ((1 + interestRate) ** years - 1)

    # Prints monthly payment on next line and reformat the string to a float using 2 decimal places
    return mortgagePayment
def data(request, year, amount, mortgage):
    parametr = Parametr.objects.last()

    data = {}

    kiraye_kof = parametr.kiraye_kofisent_tr #0.04889
    kiraye_kof_az = parametr.kiraye_kofisent_az #0.03111
    interest_rate_percent = parametr.loan_interest_rate_tr #7.08
    interest_rate__percent_az = parametr.loan_interest_rate_az #6.5

    rental_growth_tr = parametr.rental_growth_tr #5.9
    rental_growth_az = parametr.rental_growth_az #4

    appraisal_rate = parametr.appraisal_rate_tr #0.073
    appraisal_rate_az = parametr.appraisal_rate_az #0.05
    appraisal = appraisal_rate + 1
    appraisal_az = appraisal_rate_az + 1
    first_amount = amount
    leverage = amount * parametr.leverage_tr #0.8
    estate_investment = first_amount+leverage
    monthly_loan_tr = calculate_mortgage(leverage, year, interest_rate_percent)
    monthly_loan_az = calculate_mortgage(leverage, year, interest_rate__percent_az)
    diger_xerc_tr = parametr.diger_xercler_tr #600
    diger_xerc_az = parametr.diger_xercler_az #600
    heyat_sigorta_tr = parametr.heyat_sigortasi_tr #120
    heyat_sigorta_az = parametr.heyat_sigortasi_az #300

    diger_xercler_precent_tr = 0.05
    diger_xercler_precent_az = 0.05


    interest_rate_bank_az = parametr.interest_rate_bank #3

    # ---------------------------------------------------------------------------------------------
    #Turkey
    # ---------------------------------------------------------------------------------------------
    y1_value = estate_investment * appraisal
    y2_value = (y1_value) * appraisal
    y3_value = (y2_value ) * appraisal
    y4_value = (y3_value ) * appraisal
    y5_value = (y4_value ) * appraisal
    y6_value = (y5_value ) * appraisal
    y7_value = (y6_value ) * appraisal
    y8_value = (y7_value ) * appraisal
    y9_value = (y8_value ) * appraisal
    y10_value = (y9_value ) * appraisal

    y1_growth = estate_investment * appraisal_rate
    y2_growth = (y1_growth + estate_investment) * appraisal_rate
    y3_growth = (y1_growth + y2_growth + estate_investment) * appraisal_rate
    y4_growth = (y1_growth + y2_growth + y3_growth + estate_investment) * appraisal_rate
    y5_growth = (y1_growth + y2_growth + y3_growth + y4_growth + estate_investment) * appraisal_rate
    y6_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + estate_investment) * appraisal_rate
    y7_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + estate_investment) * appraisal_rate
    y8_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + estate_investment) * appraisal_rate
    y9_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + y8_growth + estate_investment) * appraisal_rate
    y10_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + y8_growth + y9_growth + estate_investment) * appraisal_rate

    y1_val = (y1_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + estate_investment * kiraye_kof)
    y1_yatirim_net_deyeri = estate_investment - 9 * monthly_loan_tr * 12 + y1_val

    y2_val = (y2_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + estate_investment * kiraye_kof * (1 + rental_growth_tr / 100))
    y2_yatirim_net_deyeri = estate_investment - 8 * monthly_loan_tr * 12 + y1_val+y2_val

    x3 = estate_investment * kiraye_kof * (1 + rental_growth_tr / 100) * (1 + rental_growth_tr / 100)
    y3_val = (y3_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x3)
    y3_yatirim_net_deyeri = estate_investment - 7 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val

    x4 = x3 * (1 + rental_growth_tr / 100)
    y4_val = (y4_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x4)
    y4_yatirim_net_deyeri =  estate_investment - 6 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val

    x5 = x4 * (1 + rental_growth_tr / 100)
    y5_val = (y5_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x5)
    y5_yatirim_net_deyeri =  estate_investment - 5 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val + y5_val

    x6 = x5 * (1 + rental_growth_tr / 100)
    y6_val = (y6_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x6)
    y6_yatirim_net_deyeri =  estate_investment - 4 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val + y5_val +y6_val

    x7 = x6 * (1 + rental_growth_tr / 100)
    y7_val = (y7_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x7)
    y7_yatirim_net_deyeri =  estate_investment - 3 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val + y5_val +y6_val + y7_val

    x8 = x7 * (1 + rental_growth_tr / 100)
    y8_val = (y8_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x8)
    y8_yatirim_net_deyeri =  estate_investment - 2 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val + y5_val +y6_val + y7_val+y8_val

    x9 = x8 * (1 + rental_growth_tr / 100)
    y9_val = (y9_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x9)
    y9_yatirim_net_deyeri =  estate_investment - 1 * monthly_loan_tr * 12 + y1_val + y2_val + y3_val + y4_val + y5_val +y6_val + y7_val+y8_val+y9_val

    x10 = x9 * (1 + rental_growth_tr / 100)
    y10_val = (y10_growth - diger_xerc_tr - heyat_sigorta_tr - monthly_loan_tr * 12 + x10)
    y10_yatirim_net_deyeri =  estate_investment  + y1_val + y2_val + y3_val + y4_val + y5_val +y6_val + y7_val+y8_val+y9_val+y10_val
    if mortgage == 1:
        datatr= [round(y1_yatirim_net_deyeri, 0),
                          round(y2_yatirim_net_deyeri, 0),
                          round(y3_yatirim_net_deyeri, 0),
                          round(y4_yatirim_net_deyeri, 0),
                          round(y5_yatirim_net_deyeri, 0),
                          round(y6_yatirim_net_deyeri, 0),
                          round(y7_yatirim_net_deyeri, 0),
                          round(y8_yatirim_net_deyeri, 0),
                          round(y9_yatirim_net_deyeri, 0),
                          round(y10_yatirim_net_deyeri, 0)]

        data['datatr'] = datatr[:year]

    y1_value = estate_investment * appraisal
    y2_value = (y1_value) * appraisal
    y3_value = (y2_value) * appraisal
    y4_value = (y3_value) * appraisal
    y5_value = (y4_value) * appraisal
    y6_value = (y5_value) * appraisal
    y7_value = (y6_value) * appraisal
    y8_value = (y7_value) * appraisal
    y9_value = (y8_value) * appraisal
    y10_value = (y9_value) * appraisal

    y1_growth = amount * appraisal_rate
    y2_growth = (y1_growth + amount) * appraisal_rate
    y3_growth = (y1_growth + y2_growth + amount) * appraisal_rate
    y4_growth = (y1_growth + y2_growth + y3_growth + amount) * appraisal_rate
    y5_growth = (y1_growth + y2_growth + y3_growth + y4_growth + amount) * appraisal_rate
    y6_growth = (y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + amount) * appraisal_rate
    y7_growth = (
                        y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + amount) * appraisal_rate
    y8_growth = (
                        y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + amount) * appraisal_rate
    y9_growth = (
                        y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + y8_growth + amount) * appraisal_rate
    y10_growth = (
                         y1_growth + y2_growth + y3_growth + y4_growth + y5_growth + y6_growth + y7_growth + y8_growth + y9_growth + amount) * appraisal_rate

    y1_val = (y1_growth - diger_xerc_tr + amount * kiraye_kof)
    y1_yatirim_net_deyeri_nagd = amount + y1_val

    y2_val = (y2_growth - diger_xerc_tr + amount * kiraye_kof * (1 + rental_growth_tr / 100))
    y2_yatirim_net_deyeri_nagd = amount + y1_val + y2_val

    x3 = amount * kiraye_kof * (1 + rental_growth_tr / 100) * (1 + rental_growth_tr / 100)
    y3_val = (y3_growth - diger_xerc_tr + x3)
    y3_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val

    x4 = x3 * (1 + rental_growth_tr / 100)
    y4_val = (y4_growth - diger_xerc_tr + x4)
    y4_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val

    x5 = x4 * (1 + rental_growth_tr / 100)
    y5_val = (y5_growth - diger_xerc_tr + x5)
    y5_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val

    x6 = x5 * (1 + rental_growth_tr / 100)
    y6_val = (y6_growth - diger_xerc_tr + x6)
    y6_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val

    x7 = x6 * (1 + rental_growth_tr / 100)
    y7_val = (y7_growth - diger_xerc_tr + x7)
    y7_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val

    x8 = x7 * (1 + rental_growth_tr / 100)
    y8_val = (y8_growth - diger_xerc_tr + x8)
    y8_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val

    x9 = x8 * (1 + rental_growth_tr / 100)
    y9_val = (y9_growth - diger_xerc_tr + x9)
    y9_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val + y9_val

    x10 = x9 * (1 + rental_growth_tr / 100)
    y10_val = (y10_growth - diger_xerc_tr + x10)
    y10_yatirim_net_deyeri_nagd = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val + y9_val + y10_val
    if mortgage != 1:
        datatr = [round(y1_yatirim_net_deyeri_nagd, 0),
                  round(y2_yatirim_net_deyeri_nagd, 0),
                  round(y3_yatirim_net_deyeri_nagd, 0),
                  round(y4_yatirim_net_deyeri_nagd, 0),
                  round(y5_yatirim_net_deyeri_nagd, 0),
                  round(y6_yatirim_net_deyeri_nagd, 0),
                  round(y7_yatirim_net_deyeri_nagd, 0),
                  round(y8_yatirim_net_deyeri_nagd, 0),
                  round(y9_yatirim_net_deyeri_nagd, 0),
                  round(y10_yatirim_net_deyeri_nagd, 0)]

        data['datatr'] = datatr[:year]


    #--------------------TR----------------------------
    if mortgage == 1:
        kiraye1 = estate_investment*kiraye_kof
        kiraye2 = kiraye1*(1+rental_growth_tr/100)
        kiraye3 = kiraye2*(1+rental_growth_tr/100)
        kiraye4 = kiraye3*(1+rental_growth_tr/100)
        kiraye5 = kiraye4*(1+rental_growth_tr/100)
        kiraye6 = kiraye5*(1+rental_growth_tr/100)
        kiraye7 = kiraye6*(1+rental_growth_tr/100)
        kiraye8 = kiraye7*(1+rental_growth_tr/100)
        kiraye9 = kiraye8*(1+rental_growth_tr/100)
        kiraye10 = kiraye9*(1+rental_growth_tr/100)

        deyer_toplam1 = estate_investment+y1_growth
        deyer_toplam2 = estate_investment + y1_growth+y2_growth

        deyer_toplam3 = estate_investment + y1_growth+y2_growth+y3_growth
        deyer_toplam4 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth
        deyer_toplam5 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth
        deyer_toplam6 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth+y6_growth
        deyer_toplam7 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth+y6_growth+y7_growth
        deyer_toplam8 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth+y6_growth+y7_growth+y8_growth
        deyer_toplam9 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth+y6_growth+y7_growth+y8_growth+y9_growth
        deyer_toplam10 = estate_investment + y1_growth+y2_growth+y3_growth+y4_growth+y5_growth+y6_growth+y7_growth+y8_growth+y9_growth+y10_growth
    else:
        kiraye1 = amount * kiraye_kof
        kiraye2 = kiraye1 * (1 + rental_growth_tr / 100)
        kiraye3 = kiraye2 * (1 + rental_growth_tr / 100)
        kiraye4 = kiraye3 * (1 + rental_growth_tr / 100)
        kiraye5 = kiraye4 * (1 + rental_growth_tr / 100)
        kiraye6 = kiraye5 * (1 + rental_growth_tr / 100)
        kiraye7 = kiraye6 * (1 + rental_growth_tr / 100)
        kiraye8 = kiraye7 * (1 + rental_growth_tr / 100)
        kiraye9 = kiraye8 * (1 + rental_growth_tr / 100)
        kiraye10 = kiraye9 * (1 + rental_growth_tr / 100)

        y1_growth_net = amount * appraisal_rate
        y2_growth_net = (y1_growth_net + amount) * appraisal_rate
        y3_growth_net = (y1_growth_net + y2_growth_net + amount) * appraisal_rate
        y4_growth_net = (y1_growth_net + y2_growth_net + y3_growth_net + amount) * appraisal_rate
        y5_growth_net = (
                                    y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + amount) * appraisal_rate
        y6_growth_net = (
                                    y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + amount) * appraisal_rate
        y7_growth_net = (
                                    y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + amount) * appraisal_rate
        y8_growth_net = (
                                    y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + amount) * appraisal_rate
        y9_growth_net = (
                                    y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + y8_growth_net + amount) * appraisal_rate
        y10_growth_net = (
                                     y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + y8_growth_net + y9_growth_net + amount) * appraisal_rate

        deyer_toplam1 = amount + y1_growth_net
        deyer_toplam2 = amount + y1_growth_net + y2_growth_net

        deyer_toplam3 = amount + y1_growth_net + y2_growth_net + y3_growth_net
        deyer_toplam4 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net
        deyer_toplam5 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net
        deyer_toplam6 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net
        deyer_toplam7 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net
        deyer_toplam8 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + y8_growth_net
        deyer_toplam9 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + y8_growth_net + y9_growth_net
        deyer_toplam10 = amount + y1_growth_net + y2_growth_net + y3_growth_net + y4_growth_net + y5_growth_net + y6_growth_net + y7_growth_net + y8_growth_net + y9_growth_net + y10_growth_net

    #--------------------TR----------------------------

    #---------------------------------------------------------------------------------------------
    # AZ
    #---------------------------------------------------------------------------------------------
    y1_value_az = estate_investment * appraisal_az
    y2_value_az = (y1_value_az) * appraisal_az
    y3_value_az = (y2_value_az) * appraisal_az
    y4_value_az = (y3_value_az) * appraisal_az
    y5_value_az = (y4_value_az) * appraisal_az
    y6_value_az = (y5_value_az) * appraisal_az
    y7_value_az = (y6_value_az) * appraisal_az
    y8_value_az = (y7_value_az) * appraisal_az
    y9_value_az = (y8_value_az) * appraisal_az
    y10_value_az = (y9_value_az) * appraisal_az

    y1_growth_az = estate_investment * appraisal_rate_az
    y2_growth_az = (y1_growth_az + estate_investment) * appraisal_rate_az
    y3_growth_az = (y1_growth_az + y2_growth_az + estate_investment) * appraisal_rate_az
    y4_growth_az = (y1_growth_az + y2_growth_az + y3_growth_az + estate_investment) * appraisal_rate_az
    y5_growth_az = (y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + estate_investment) * appraisal_rate_az
    y6_growth_az = (
                               y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + estate_investment) * appraisal_rate_az
    y7_growth_az = (
                               y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + estate_investment) * appraisal_rate_az
    y8_growth_az = (
                               y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + estate_investment) * appraisal_rate_az
    y9_growth_az = (
                               y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + y8_growth_az + estate_investment) * appraisal_rate_az
    y10_growth_az = (
                                y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + y8_growth_az + y9_growth_az + estate_investment) * appraisal_rate_az

    y1_val_az = (y1_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + estate_investment * kiraye_kof_az)
    y1_yatirim_net_deyeri_az = \
        estate_investment - \
        9 * monthly_loan_az * 12 + \
        y1_val_az







    y2_val_az = (
                y2_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + estate_investment * kiraye_kof_az * (
                    1 + rental_growth_az / 100))
    y2_yatirim_net_deyeri_az = estate_investment - 8 * monthly_loan_az * 12 + y1_val_az + y2_val_az

    x3 = estate_investment * kiraye_kof_az * (1 + rental_growth_az / 100) * (1 + rental_growth_az / 100)
    y3_val_az = (y3_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x3)
    y3_yatirim_net_deyeri_az = estate_investment - 7 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az

    x4 = x3 * (1 + rental_growth_az / 100)
    y4_val_az = (y4_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x4)
    y4_yatirim_net_deyeri_az = estate_investment - 6 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az

    x5 = x4 * (1 + rental_growth_az / 100)
    y5_val_az = (y5_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x5)
    y5_yatirim_net_deyeri_az = estate_investment - 5 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az

    x6 = x5 * (1 + rental_growth_az / 100)
    y6_val_az = (y6_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x6)
    y6_yatirim_net_deyeri_az = estate_investment - 4 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az

    x7 = x6 * (1 + rental_growth_az / 100)
    y7_val_az = (y7_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x7)
    y7_yatirim_net_deyeri_az = estate_investment - 3 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az

    x8 = x7 * (1 + rental_growth_az / 100)
    y8_val_az = (y8_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x8)
    y8_yatirim_net_deyeri_az = estate_investment - 2 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az

    x9 = x8 * (1 + rental_growth_az / 100)
    y9_val_az = (y9_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x9)
    y9_yatirim_net_deyeri_az = estate_investment - 1 * monthly_loan_az * 12 + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az

    x10 = x9 * (1 + rental_growth_az / 100)
    y10_val_az = (y10_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + x10)
    y10_yatirim_net_deyeri_az = estate_investment + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az + y10_val_az





    if mortgage == 1:
        dataaz = [round(y1_yatirim_net_deyeri_az, 0),
                          round(y2_yatirim_net_deyeri_az, 0),
                          round(y3_yatirim_net_deyeri_az, 0),
                          round(y4_yatirim_net_deyeri_az, 0),
                          round(y5_yatirim_net_deyeri_az, 0),
                          round(y6_yatirim_net_deyeri_az, 0),
                          round(y7_yatirim_net_deyeri_az, 0),
                          round(y8_yatirim_net_deyeri_az, 0),
                          round(y9_yatirim_net_deyeri_az, 0),
                          round(y10_yatirim_net_deyeri_az, 0)]
        data['dataaz'] = dataaz[:year]

    y1_value_az = amount * appraisal_az
    y2_value_az = (y1_value_az) * appraisal_az
    y3_value_az = (y2_value_az) * appraisal_az
    y4_value_az = (y3_value_az) * appraisal_az
    y5_value_az = (y4_value_az) * appraisal_az
    y6_value_az = (y5_value_az) * appraisal_az
    y7_value_az = (y6_value_az) * appraisal_az
    y8_value_az = (y7_value_az) * appraisal_az
    y9_value_az = (y8_value_az) * appraisal_az
    y10_value_az = (y9_value_az) * appraisal_az

    y1_growth_az = amount * appraisal_rate_az
    y2_growth_az = (y1_growth_az + amount) * appraisal_rate_az
    y3_growth_az = (y1_growth_az + y2_growth_az + amount) * appraisal_rate_az
    y4_growth_az = (y1_growth_az + y2_growth_az + y3_growth_az + amount) * appraisal_rate_az
    y5_growth_az = (y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + amount) * appraisal_rate_az
    y6_growth_az = (
                           y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + amount) * appraisal_rate_az
    y7_growth_az = (
                           y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + amount) * appraisal_rate_az
    y8_growth_az = (
                           y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + amount) * appraisal_rate_az
    y9_growth_az = (
                           y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + y8_growth_az + amount) * appraisal_rate_az
    y10_growth_az = (
                            y1_growth_az + y2_growth_az + y3_growth_az + y4_growth_az + y5_growth_az + y6_growth_az + y7_growth_az + y8_growth_az + y9_growth_az + amount) * appraisal_rate_az

    y1_val_az = ( y1_growth_az - diger_xerc_az + amount * kiraye_kof_az)
    y1_yatirim_net_deyeri_az_nagd = amount + y1_val_az







    y2_val_az = (y2_growth_az - diger_xerc_az + amount * kiraye_kof_az * (1 + rental_growth_az / 100))
    y2_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az






    x3 = amount * kiraye_kof_az * (1 + rental_growth_az / 100) * (1 + rental_growth_az / 100)
    y3_val_az = (y3_growth_az - diger_xerc_az + x3)
    y3_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az

    x4 = x3 * (1 + rental_growth_az / 100)
    y4_val_az = (y4_growth_az - diger_xerc_az + x4)
    y4_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az

    x5 = x4 * (1 + rental_growth_az / 100)
    y5_val_az = (y5_growth_az - diger_xerc_az + x5)
    y5_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az

    x6 = x5 * (1 + rental_growth_az / 100)
    y6_val_az = (y6_growth_az - diger_xerc_az + x6)
    y6_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az

    x7 = x6 * (1 + rental_growth_az / 100)
    y7_val_az = (y7_growth_az - diger_xerc_az + x7)
    y7_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az

    x8 = x7 * (1 + rental_growth_az / 100)
    y8_val_az = (y8_growth_az - diger_xerc_az + x8)
    y8_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az

    x9 = x8 * (1 + rental_growth_az / 100)
    y9_val_az = (y9_growth_az - diger_xerc_az + x9)
    y9_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az

    x10 = x9 * (1 + rental_growth_az / 100)
    y10_val_az = (y10_growth_az - diger_xerc_az + x10)
    y10_yatirim_net_deyeri_az_nagd = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az + y10_val_az

    if mortgage != 1:
        dataaz = [round(y1_yatirim_net_deyeri_az_nagd, 0),
                   round(y2_yatirim_net_deyeri_az_nagd, 0),
                   round(y3_yatirim_net_deyeri_az_nagd, 0),
                   round(y4_yatirim_net_deyeri_az_nagd, 0),
                   round(y5_yatirim_net_deyeri_az_nagd, 0),
                   round(y6_yatirim_net_deyeri_az_nagd, 0),
                   round(y7_yatirim_net_deyeri_az_nagd, 0),
                   round(y8_yatirim_net_deyeri_az_nagd, 0),
                   round(y9_yatirim_net_deyeri_az_nagd, 0),
                   round(y10_yatirim_net_deyeri_az_nagd, 0)]

        data['dataaz'] = dataaz[:year]

    # ---------------------------------------------------------------------------------------------
    #Bank
    # ---------------------------------------------------------------------------------------------
    yx1 = amount * interest_rate_bank_az/100
    y1_yatirim_net_deyeri_bank = amount+yx1

    yx2 = (amount+yx1)* interest_rate_bank_az/100
    y2_yatirim_net_deyeri_bank = amount+yx1+yx2

    yx3 = (amount+yx1+yx2)*0.035
    y3_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3

    yx4 = (amount+yx1+yx2+yx3)*0.035
    y4_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4

    yx5 = (amount+yx1+yx2+yx3+yx4)*0.035
    y5_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5

    yx6 = (amount+yx1+yx2+yx3+yx4+yx5)*0.035
    y6_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5+yx6

    yx7 = (amount+yx1+yx2+yx3+yx4+yx5+yx6)*0.035
    y7_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7

    yx8 = (amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7)*0.035
    y8_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8

    yx9 = (amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8)*0.035
    y9_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8+yx9

    yx10 = (amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8+yx9)*0.035
    y10_yatirim_net_deyeri_bank = amount+yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8+yx9+yx10

    databank = [round(y1_yatirim_net_deyeri_bank, 0),
                        round(y2_yatirim_net_deyeri_bank, 0),
                        round(y3_yatirim_net_deyeri_bank, 0),
                      round(y4_yatirim_net_deyeri_bank, 0),
                        round(y5_yatirim_net_deyeri_bank, 0),
                        round(y6_yatirim_net_deyeri_bank, 0),
                      round(y7_yatirim_net_deyeri_bank, 0),
                        round(y8_yatirim_net_deyeri_bank, 0),
                        round(y9_yatirim_net_deyeri_bank, 0),
                      round(y10_yatirim_net_deyeri_bank, 0)]
    data['databank'] = databank[:year]


    # ---------------------------------------------------------------------------------------------
    #Turkey Net
    # ---------------------------------------------------------------------------------------------



    # ---------------------------------------------------------------------------------------------
    # Azerbaijan Net
    # ---------------------------------------------------------------------------------------------




    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------



    y1_value_az = estate_investment * appraisal_az
    y2_value_az = (y1_value_az) * appraisal_az
    y3_value_az = (y2_value_az) * appraisal_az
    y4_value_az = (y3_value_az) * appraisal_az
    y5_value_az = (y4_value_az) * appraisal_az
    y6_value_az = (y5_value_az) * appraisal_az
    y7_value_az = (y6_value_az) * appraisal_az
    y8_value_az = (y7_value_az) * appraisal_az
    y9_value_az = (y8_value_az) * appraisal_az
    y10_value_az = (y9_value_az) * appraisal_az

    y1_value_bank = estate_investment * appraisal
    y2_value_bank = (y1_value_bank) * appraisal
    y3_value_bank = (y2_value_bank) * appraisal
    y4_value_bank = (y3_value_bank) * appraisal
    y5_value_bank = (y4_value_bank) * appraisal
    y6_value_bank = (y5_value_bank) * appraisal
    y7_value_bank = (y6_value_bank) * appraisal
    y8_value_bank = (y7_value_bank) * appraisal
    y9_value_bank = (y8_value_bank) * appraisal
    y10_value_bank = (y9_value_bank) * appraisal

    y1_value2 = estate_investment * appraisal
    y2_value2 = (y1_value2) * appraisal
    y3_value2 = (y2_value2) * appraisal
    y4_value2 = (y3_value2) * appraisal
    y5_value2 = (y4_value2) * appraisal
    y6_value2 = (y5_value2) * appraisal
    y7_value2 = (y6_value2) * appraisal
    y8_value2 = (y7_value2) * appraisal
    y9_value2 = (y8_value2) * appraisal
    y10_value2 = (y9_value2) * appraisal

    y1_value2_az = estate_investment * appraisal_az
    y2_value2_az = (y1_value2_az) * appraisal_az
    y3_value2_az = (y2_value2_az) * appraisal_az
    y4_value2_az = (y3_value2_az) * appraisal_az
    y5_value2_az = (y4_value2_az) * appraisal_az
    y6_value2_az = (y5_value2_az) * appraisal_az
    y7_value2_az = (y6_value2_az) * appraisal_az
    y8_value2_az = (y7_value2_az) * appraisal_az
    y9_value2_az = (y8_value2_az) * appraisal_az
    y10_value2_az = (y9_value2_az) * appraisal_az






    ###---------- Əmlakın Dəyəri Türkiyə
    if mortgage == 1:
        deyertr_artimi_1 = estate_investment * appraisal_rate
        deyer_tr_1 = estate_investment + estate_investment * appraisal_rate

        deyertr_artimi_2 = deyer_tr_1 * appraisal_rate
        deyer_tr_2 = deyer_tr_1+deyertr_artimi_2

        deyertr_artimi_3 = deyer_tr_2 * appraisal_rate
        deyer_tr_3 = deyer_tr_2+deyertr_artimi_3

        deyertr_artimi_4 = deyer_tr_3 * appraisal_rate
        deyer_tr_4 = deyer_tr_3+deyertr_artimi_4

        deyertr_artimi_5 = deyer_tr_4 * appraisal_rate
        deyer_tr_5 = deyer_tr_4+deyertr_artimi_5

        deyertr_artimi_6 = deyer_tr_5 * appraisal_rate
        deyer_tr_6 = deyer_tr_5+deyertr_artimi_6

        deyertr_artimi_7 = deyer_tr_6 * appraisal_rate
        deyer_tr_7 = deyer_tr_6+deyertr_artimi_7

        deyertr_artimi_8 = deyer_tr_7 * appraisal_rate
        deyer_tr_8 = deyer_tr_7+deyertr_artimi_8

        deyertr_artimi_9 = deyer_tr_8 * appraisal_rate
        deyer_tr_9 = deyer_tr_8+deyertr_artimi_9

        deyertr_artimi_10 = deyer_tr_9 * appraisal_rate
        deyer_tr_10 = deyer_tr_9+deyertr_artimi_10



        deyertr = [round(deyer_tr_1, 0),
                   round(deyer_tr_2, 0),
                   round(deyer_tr_3, 0),
                   round(deyer_tr_4, 0),
                   round(deyer_tr_5, 0),
                   round(deyer_tr_6, 0),
                   round(deyer_tr_7, 0),
                   round(deyer_tr_8, 0),
                   round(deyer_tr_9, 0),
                   round(deyer_tr_10, 0)]


        data['deyertr'] = deyertr[:year]
    else:
        deyertr_artimi_1 = amount * appraisal_rate
        deyer_tr_1 = amount + amount * appraisal_rate

        deyertr_artimi_2 = deyer_tr_1 * appraisal_rate
        deyer_tr_2 = deyer_tr_1 + deyertr_artimi_2

        deyertr_artimi_3 = deyer_tr_2 * appraisal_rate
        deyer_tr_3 = deyer_tr_2 + deyertr_artimi_3

        deyertr_artimi_4 = deyer_tr_3 * appraisal_rate
        deyer_tr_4 = deyer_tr_3 + deyertr_artimi_4

        deyertr_artimi_5 = deyer_tr_4 * appraisal_rate
        deyer_tr_5 = deyer_tr_4 + deyertr_artimi_5

        deyertr_artimi_6 = deyer_tr_5 * appraisal_rate
        deyer_tr_6 = deyer_tr_5 + deyertr_artimi_6

        deyertr_artimi_7 = deyer_tr_6 * appraisal_rate
        deyer_tr_7 = deyer_tr_6 + deyertr_artimi_7

        deyertr_artimi_8 = deyer_tr_7 * appraisal_rate
        deyer_tr_8 = deyer_tr_7 + deyertr_artimi_8

        deyertr_artimi_9 = deyer_tr_8 * appraisal_rate
        deyer_tr_9 = deyer_tr_8 + deyertr_artimi_9

        deyertr_artimi_10 = deyer_tr_9 * appraisal_rate
        deyer_tr_10 = deyer_tr_9 + deyertr_artimi_10

        deyertr = [round(deyer_tr_1, 0),
                   round(deyer_tr_2, 0),
                   round(deyer_tr_3, 0),
                   round(deyer_tr_4, 0),
                   round(deyer_tr_5, 0),
                   round(deyer_tr_6, 0),
                   round(deyer_tr_7, 0),
                   round(deyer_tr_8, 0),
                   round(deyer_tr_9, 0),
                   round(deyer_tr_10, 0)]

        data['deyertr'] = deyertr[:year]

    data['field1'] = 120000

    data['year'] = year

    if year == 1:
        data['kiraye'] = round(kiraye1, 0)
        data['deyer'] = round(deyer_tr_1, 0)
    elif year == 2:
        data['kiraye'] = round(kiraye1 + kiraye2, 0)
        data['deyer'] = round(deyer_tr_2, 0)
    elif year == 3:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3, 0)
        data['deyer'] = round(deyer_tr_3, 0)
    elif year == 4:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4, 0)
        data['deyer'] = round(deyer_tr_4, 0)
    elif year == 5:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5, 0)
        data['deyer'] = round(deyer_tr_5, 0)
    elif year == 6:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6, 0)
        data['deyer'] = round(deyer_tr_6, 0)
    elif year == 7:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7, 0)
        data['deyer'] = round(deyer_tr_7, 0)
    elif year == 8:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8, 0)
        data['deyer'] = round(deyer_tr_8, 0)
    elif year == 9:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8 + kiraye9,
                               0)
        data['deyer'] = round(deyer_tr_9, 0)
    elif year == 10:
        data['kiraye'] = round(
            kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8 + kiraye9 + kiraye10, 0)
        data['deyer'] = round(deyer_tr_10, 0)
    ###---------- Əmlakın Dəyəri Azərbaycan
    if mortgage == 1:
        deyeraz_artimi_1 = estate_investment * appraisal_rate_az
        deyer_az_1 = estate_investment + estate_investment * appraisal_rate_az

        deyeraz_artimi_2 = deyer_az_1 * appraisal_rate_az
        deyer_az_2 = deyer_az_1 + deyeraz_artimi_2

        deyeraz_artimi_3 = deyer_az_2 * appraisal_rate_az
        deyer_az_3 = deyer_az_2 + deyeraz_artimi_3

        deyeraz_artimi_4 = deyer_az_3 * appraisal_rate_az
        deyer_az_4 = deyer_az_3 + deyeraz_artimi_4

        deyeraz_artimi_5 = deyer_az_4 * appraisal_rate_az
        deyer_az_5 = deyer_az_4 + deyeraz_artimi_5

        deyeraz_artimi_6 = deyer_az_5 * appraisal_rate_az
        deyer_az_6 = deyer_az_5 + deyeraz_artimi_6

        deyeraz_artimi_7 = deyer_az_6 * appraisal_rate_az
        deyer_az_7 = deyer_az_6 + deyeraz_artimi_7

        deyeraz_artimi_8 = deyer_az_7 * appraisal_rate_az
        deyer_az_8 = deyer_az_7 + deyeraz_artimi_8

        deyeraz_artimi_9 = deyer_az_8 * appraisal_rate_az
        deyer_az_9 = deyer_az_8 + deyeraz_artimi_9

        deyeraz_artimi_10 = deyer_az_9 * appraisal_rate_az
        deyer_az_10 = deyer_az_9 + deyeraz_artimi_10

        deyeraz = [round(deyer_az_1, 0),
                   round(deyer_az_2, 0),
                   round(deyer_az_3, 0),
                   round(deyer_az_4, 0),
                   round(deyer_az_5, 0),
                   round(deyer_az_6, 0),
                   round(deyer_az_7, 0),
                   round(deyer_az_8, 0),
                   round(deyer_az_9, 0),
                   round(deyer_az_10, 0)]

        data['deyeraz'] = deyeraz[:year]
    else:
        deyeraz_artimi_1 = amount * appraisal_rate_az
        deyer_az_1 = amount + amount * appraisal_rate_az

        deyeraz_artimi_2 = deyer_az_1 * appraisal_rate_az
        deyer_az_2 = deyer_az_1 + deyeraz_artimi_2

        deyeraz_artimi_3 = deyer_az_2 * appraisal_rate_az
        deyer_az_3 = deyer_az_2 + deyeraz_artimi_3

        deyeraz_artimi_4 = deyer_az_3 * appraisal_rate_az
        deyer_az_4 = deyer_az_3 + deyeraz_artimi_4

        deyeraz_artimi_5 = deyer_az_4 * appraisal_rate_az
        deyer_az_5 = deyer_az_4 + deyeraz_artimi_5

        deyeraz_artimi_6 = deyer_az_5 * appraisal_rate_az
        deyer_az_6 = deyer_az_5 + deyeraz_artimi_6

        deyeraz_artimi_7 = deyer_az_6 * appraisal_rate_az
        deyer_az_7 = deyer_az_6 + deyeraz_artimi_7

        deyeraz_artimi_8 = deyer_az_7 * appraisal_rate_az
        deyer_az_8 = deyer_az_7 + deyeraz_artimi_8

        deyeraz_artimi_9 = deyer_az_8 * appraisal_rate_az
        deyer_az_9 = deyer_az_8 + deyeraz_artimi_9

        deyeraz_artimi_10 = deyer_az_9 * appraisal_rate_az
        deyer_az_10 = deyer_az_9 + deyeraz_artimi_10

        deyeraz = [round(deyer_az_1, 0),
                   round(deyer_az_2, 0),
                   round(deyer_az_3, 0),
                   round(deyer_az_4, 0),
                   round(deyer_az_5, 0),
                   round(deyer_az_6, 0),
                   round(deyer_az_7, 0),
                   round(deyer_az_8, 0),
                   round(deyer_az_9, 0),
                   round(deyer_az_10, 0)]

        data['deyeraz'] = deyeraz[:year]

    ###---------- Yatırım qazancı Türkiyə
    if mortgage == 1:
        diger_xercler = (estate_investment)*diger_xercler_precent_tr
        yatirim_qazanci_tr_1 = y1_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_2 = y2_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_3 = y3_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_4 = y4_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_5 = y5_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_6 = y6_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_7 = y7_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_8 = y8_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_9 = y9_yatirim_net_deyeri-amount-diger_xercler
        yatirim_qazanci_tr_10 = y10_yatirim_net_deyeri-amount-diger_xercler



        yatirim_qazanci_tr = [round(yatirim_qazanci_tr_1, 0),
                   round(yatirim_qazanci_tr_2, 0),
                   round(yatirim_qazanci_tr_3, 0),
                   round(yatirim_qazanci_tr_4, 0),
                   round(yatirim_qazanci_tr_5, 0),
                   round(yatirim_qazanci_tr_6, 0),
                   round(yatirim_qazanci_tr_7, 0),
                   round(yatirim_qazanci_tr_8, 0),
                   round(yatirim_qazanci_tr_9, 0),
                   round(yatirim_qazanci_tr_10, 0)]

        data['yatirim_qazanci_tr'] = yatirim_qazanci_tr[:year]
    else:
        diger_xercler = (amount) * diger_xercler_precent_tr
        yatirim_qazanci_tr_1 = y1_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_2 = y2_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_3 = y3_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_4 = y4_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_5 = y5_yatirim_net_deyeri_nagd - amount - diger_xercler


        yatirim_qazanci_tr_6 = y6_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_7 = y7_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_8 = y8_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_9 = y9_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr_10 = y10_yatirim_net_deyeri_nagd - amount - diger_xercler
        yatirim_qazanci_tr = [round(yatirim_qazanci_tr_1, 0),
                              round(yatirim_qazanci_tr_2, 0),
                              round(yatirim_qazanci_tr_3, 0),
                              round(yatirim_qazanci_tr_4, 0),
                              round(yatirim_qazanci_tr_5, 0),
                              round(yatirim_qazanci_tr_6, 0),
                              round(yatirim_qazanci_tr_7, 0),
                              round(yatirim_qazanci_tr_8, 0),
                              round(yatirim_qazanci_tr_9, 0),
                              round(yatirim_qazanci_tr_10, 0)]

        data['yatirim_qazanci_tr'] = yatirim_qazanci_tr[:year]
    ###---------- Yatırım qazancı Azərbaycan
    if mortgage == 1:

        diger_xercler_az_xx = (amount) * diger_xercler_precent_az
        yatirim_qazanci_az_1 = y1_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_2 = y2_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_3 = y3_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_4 = y4_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_5 = y5_yatirim_net_deyeri_az - amount - diger_xercler_az_xx


        yatirim_qazanci_az_6 = y6_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_7 = y7_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_8 = y8_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_9 = y9_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az_10 = y10_yatirim_net_deyeri_az - amount - diger_xercler_az_xx
        yatirim_qazanci_az = [round(yatirim_qazanci_az_1, 0),
                              round(yatirim_qazanci_az_2, 0),
                              round(yatirim_qazanci_az_3, 0),
                              round(yatirim_qazanci_az_4, 0),
                              round(yatirim_qazanci_az_5, 0),
                              round(yatirim_qazanci_az_6, 0),
                              round(yatirim_qazanci_az_7, 0),
                              round(yatirim_qazanci_az_8, 0),
                              round(yatirim_qazanci_az_9, 0),
                              round(yatirim_qazanci_az_10, 0)]

        data['yatirim_qazanci_az'] = yatirim_qazanci_az[:year]
    else:
        diger_xercler_az = (estate_investment) * diger_xercler_precent_az
        yatirim_qazanci_az_1 = y1_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_2 = y2_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_3 = y3_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_4 = y4_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_5 = y5_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az

        print("++++++++++")
        print(y5_yatirim_net_deyeri_az_nagd)
        print("++++++++++")

        yatirim_qazanci_az_6 = y6_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_7 = y7_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_8 = y8_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_9 = y9_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az_10 = y10_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az
        yatirim_qazanci_az = [round(yatirim_qazanci_az_1, 0),
                              round(yatirim_qazanci_az_2, 0),
                              round(yatirim_qazanci_az_3, 0),
                              round(yatirim_qazanci_az_4, 0),
                              round(yatirim_qazanci_az_5, 0),
                              round(yatirim_qazanci_az_6, 0),
                              round(yatirim_qazanci_az_7, 0),
                              round(yatirim_qazanci_az_8, 0),
                              round(yatirim_qazanci_az_9, 0),
                              round(yatirim_qazanci_az_10, 0)]

        data['yatirim_qazanci_az'] = yatirim_qazanci_az[:year]

    ###---------- Qazanc marjası Türkiyə
    if mortgage == 1:
        diger_xercler_tr_marja_ipoteka = (estate_investment) * diger_xercler_precent_tr
        yatirim_qazanci_marja_tr_1 = (y1_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_2 = (y2_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_3 = (y3_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_4 = (y4_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_5 = (y5_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100

        yatirim_qazanci_marja_tr_6 = (y6_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_7 = (y7_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_8 = (y8_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_9 = (y9_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr_10 = (y10_yatirim_net_deyeri-amount-diger_xercler_tr_marja_ipoteka)/(amount+diger_xercler_tr_marja_ipoteka)*100
        yatirim_qazanci_marja_tr = [round(yatirim_qazanci_marja_tr_1, 0),
                                    round(yatirim_qazanci_marja_tr_2, 0),
                                    round(yatirim_qazanci_marja_tr_3, 0),
                                    round(yatirim_qazanci_marja_tr_4, 0),
                                    round(yatirim_qazanci_marja_tr_5, 0),
                                    round(yatirim_qazanci_marja_tr_6, 0),
                                    round(yatirim_qazanci_marja_tr_7, 0),
                                    round(yatirim_qazanci_marja_tr_8, 0),
                                    round(yatirim_qazanci_marja_tr_9, 0),
                                    round(yatirim_qazanci_marja_tr_10, 0)]

        data['yatirim_qazanci_marja_tr'] = yatirim_qazanci_marja_tr[:year]
    else:
        diger_xercler_tr_marja = (estate_investment) * diger_xercler_precent_tr
        yatirim_qazanci_marja_tr_1 = (y1_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_2 = (y2_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_3 = (y3_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_4 = (y4_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_5 = (y5_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100

        yatirim_qazanci_marja_tr_6 = (y6_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_7 = (y7_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_8 = (y8_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_9 = (y9_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr_10 = (y10_yatirim_net_deyeri_nagd - amount - diger_xercler_tr_marja) / (
                    amount + diger_xercler_tr_marja) * 100
        yatirim_qazanci_marja_tr = [round(yatirim_qazanci_marja_tr_1, 0),
                                    round(yatirim_qazanci_marja_tr_2, 0),
                                    round(yatirim_qazanci_marja_tr_3, 0),
                                    round(yatirim_qazanci_marja_tr_4, 0),
                                    round(yatirim_qazanci_marja_tr_5, 0),
                                    round(yatirim_qazanci_marja_tr_6, 0),
                                    round(yatirim_qazanci_marja_tr_7, 0),
                                    round(yatirim_qazanci_marja_tr_8, 0),
                                    round(yatirim_qazanci_marja_tr_9, 0),
                                    round(yatirim_qazanci_marja_tr_10, 0)]

        data['yatirim_qazanci_marja_tr'] = yatirim_qazanci_marja_tr[:year]
    ###---------- Qazanc marjası Azərbaycan
    if mortgage == 1:
        diger_xercler_az_marja_ip = (amount) * diger_xercler_precent_tr
        yatirim_qazanci_marja_az_1 = (y1_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_2 = (y2_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_3 = (y3_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_4 = (y4_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_5 = (y5_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_6 = (y6_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_7 = (y7_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_8 = (y8_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_9 = (y9_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az_10 = (y10_yatirim_net_deyeri_az - amount - diger_xercler_az_marja_ip) / (amount + diger_xercler_az_marja_ip)*100
        yatirim_qazanci_marja_az = [round(yatirim_qazanci_marja_az_1, 0),
                                    round(yatirim_qazanci_marja_az_2, 0),
                                    round(yatirim_qazanci_marja_az_3, 0),
                                    round(yatirim_qazanci_marja_az_4, 0),
                                    round(yatirim_qazanci_marja_az_5, 0),
                                    round(yatirim_qazanci_marja_az_6, 0),
                                    round(yatirim_qazanci_marja_az_7, 0),
                                    round(yatirim_qazanci_marja_az_8, 0),
                                    round(yatirim_qazanci_marja_az_9, 0),
                                    round(yatirim_qazanci_marja_az_10, 0)]

        data['yatirim_qazanci_marja_az'] = yatirim_qazanci_marja_az[:year]
    else:
        diger_xercler_az_marja_nagd = (estate_investment) * diger_xercler_precent_tr
        yatirim_qazanci_marja_az_1 = (y1_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_2 = (y2_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_3 = (y3_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_4 = (y4_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_5 = (y5_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_6 = (y6_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_7 = (y7_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_8 = (y8_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_9 = (y9_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az_10 = (y10_yatirim_net_deyeri_az_nagd - amount - diger_xercler_az_marja_nagd) / (
                    amount + diger_xercler_az_marja_nagd) * 100
        yatirim_qazanci_marja_az = [round(yatirim_qazanci_marja_az_1, 0),
                                    round(yatirim_qazanci_marja_az_2, 0),
                                    round(yatirim_qazanci_marja_az_3, 0),
                                    round(yatirim_qazanci_marja_az_4, 0),
                                    round(yatirim_qazanci_marja_az_5, 0),
                                    round(yatirim_qazanci_marja_az_6, 0),
                                    round(yatirim_qazanci_marja_az_7, 0),
                                    round(yatirim_qazanci_marja_az_8, 0),
                                    round(yatirim_qazanci_marja_az_9, 0),
                                    round(yatirim_qazanci_marja_az_10, 0)]

        data['yatirim_qazanci_marja_az'] = yatirim_qazanci_marja_az[:year]
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

        pages = Pages.objects.all()
        context = {
            'pages': pages,
            "general": general,
            "socials": socials,
            "main_section": main_section,
        }
        return render(request, "success2.html", context)

def page(request, link):
    pages = Pages.objects.all()
    page = Pages.objects.get(link=link)
    general = General.objects.last()
    socials = Social.objects.all()
    context = {
        'page': page,
        'pages': pages,
        "general": general,
        "socials": socials,
    }
    return render(request, 'page.html', context)

def contactform(request):
    general = General.objects.last()
    socials = Social.objects.all()

    main_section = MainSection.objects.last()

    if request.method == 'POST':
        name = ''
        email = ''
        phone = ''
        prefix = ''
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
        try:
            prefix = request.POST.get('prefix')
        except:
            prefix = ''
        Contact.objects.create(
            name=name,
            email=email,
            prefix=prefix,
            phone=phone
        )

        pages = Pages.objects.all()
        context = {
            'pages': pages,
            "general": general,
            "socials": socials,
            "main_section": main_section,
        }
        return render(request, "success.html", context)


def index(request):

    head = Head.objects.all()
    body = Body.objects.all()
    calendly = CalendlyScript.objects.last()
    slider = Slider.objects.all()
    if request.user_agent.is_mobile:
        is_mobile = True
    else:
        is_mobile = False
    general = General.objects.last()
    socials = Social.objects.all()
    why = Why.objects.all()
    tablar = Tablar.objects.all()
    villas = Offer.objects.filter(type='V')
    apartments = Offer.objects.filter(type="A")
    faq = FAQ.objects.all()[:5]
    total_obj = FAQ.objects.count()
    feedback = Feedback.objects.all()

    features = Feature.objects.all()
    main_section = MainSection.objects.last()
    slider_section = SliderSection.objects.last()
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
    calculator = Parametr.objects.last()
    suallar = Suallar.objects.all()
    pages = Pages.objects.all()
    context = {
        'pages': pages,
        'calendly': calendly,
        'calculator': calculator,
        'slider': slider,
        'body': body,
        'total_obj': total_obj,
        'head': head,
        'is_mobile': is_mobile,
        "sorting_sections": sorting_sections,
        "slider_section": slider_section,
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
