import os

from django.shortcuts import render
from core.models import General, Social, Why, Tablar, FAQ, Feedback, Feature
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
    data = {}

    kiraye_kof = 0.04889
    kiraye_kof_az = 0.03111
    interest_rate_percent = 7.08
    rental_growth_tr = 5.9
    rental_growth_az = 4
    interest_rate = 0.0708
    interest_rate_az = 0.065
    interest_rate__percent_az = 6.5
    appraisal_rate = 0.073
    appraisal_rate_az = 0.05
    appraisal = 1.073
    appraisal_az = 1.05
    first_amount = amount
    leverage = amount * 0.8
    estate_investment = first_amount+leverage
    monthly_loan_tr = calculate_mortgage(60000, 10, interest_rate_percent)
    monthly_loan_az = calculate_mortgage(60000, 10, interest_rate__percent_az)
    diger_xerc_tr = 600
    diger_xerc_az = 600
    heyat_sigorta_tr = 120
    heyat_sigorta_az = 240

    interest_rate_bank_az = 3

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
        print(deyer_toplam1)
        deyer_toplam2 = estate_investment + y1_growth+y2_growth
        print(deyer_toplam2)

        deyer_toplam3 = estate_investment + y1_growth+y2_growth+y3_growth
        print(deyer_toplam3)
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
        print(deyer_toplam1)
        deyer_toplam2 = amount + y1_growth_net + y2_growth_net
        print(deyer_toplam2)

        deyer_toplam3 = amount + y1_growth_net + y2_growth_net + y3_growth_net
        print(deyer_toplam3)
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

    y1_val_az = (
                y1_growth_az - diger_xerc_az - heyat_sigorta_az - monthly_loan_az * 12 + estate_investment * kiraye_kof_az)
    y1_yatirim_net_deyeri_az = estate_investment - 9 * monthly_loan_az * 12 + y1_val_az

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
    y1_yatirim_net_deyeri = amount + y1_val

    y2_val = (y2_growth - diger_xerc_tr + amount * kiraye_kof * (1 + rental_growth_tr / 100))
    y2_yatirim_net_deyeri = amount + y1_val + y2_val

    x3 = amount * kiraye_kof * (1 + rental_growth_tr / 100) * (1 + rental_growth_tr / 100)
    y3_val = (y3_growth - diger_xerc_tr + x3)
    y3_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val

    x4 = x3 * (1 + rental_growth_tr / 100)
    y4_val = (y4_growth - diger_xerc_tr + x4)
    y4_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val

    x5 = x4 * (1 + rental_growth_tr / 100)
    y5_val = (y5_growth - diger_xerc_tr + x5)
    y5_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val

    x6 = x5 * (1 + rental_growth_tr / 100)
    y6_val = (y6_growth - diger_xerc_tr + x6)
    y6_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val

    x7 = x6 * (1 + rental_growth_tr / 100)
    y7_val = (y7_growth - diger_xerc_tr + x7)
    y7_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val

    x8 = x7 * (1 + rental_growth_tr / 100)
    y8_val = (y8_growth - diger_xerc_tr + x8)
    y8_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val

    x9 = x8 * (1 + rental_growth_tr / 100)
    y9_val = (y9_growth - diger_xerc_tr + x9)
    y9_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val + y9_val

    x10 = x9 * (1 + rental_growth_tr / 100)
    y10_val = (y10_growth - diger_xerc_tr + x10)
    y10_yatirim_net_deyeri = amount + y1_val + y2_val + y3_val + y4_val + y5_val + y6_val + y7_val + y8_val + y9_val + y10_val
    datatr2 = [round(y1_yatirim_net_deyeri, 0),
               round(y2_yatirim_net_deyeri, 0),
               round(y3_yatirim_net_deyeri, 0),
               round(y4_yatirim_net_deyeri, 0),
                       round(y5_yatirim_net_deyeri, 0),
               round(y6_yatirim_net_deyeri, 0) ,
               round(y7_yatirim_net_deyeri, 0),
               round(y8_yatirim_net_deyeri, 0),
                       round(y9_yatirim_net_deyeri, 0),
               round(y10_yatirim_net_deyeri, 0)]

    data['datatr2'] = datatr2[:year]

    # ---------------------------------------------------------------------------------------------
    # Azerbaijan Net
    # ---------------------------------------------------------------------------------------------

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

    y1_val_az = (
            y1_growth_az - diger_xerc_az   + amount * kiraye_kof_az)
    y1_yatirim_net_deyeri_az = amount  + y1_val_az

    y2_val_az = (y2_growth_az - diger_xerc_az   + amount * kiraye_kof_az * (1 + rental_growth_az / 100))
    y2_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az



    x3 = amount * kiraye_kof_az * (1 + rental_growth_az / 100) * (1 + rental_growth_az / 100)
    y3_val_az = (y3_growth_az - diger_xerc_az   + x3)
    y3_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az

    x4 = x3 * (1 + rental_growth_az / 100)
    y4_val_az = (y4_growth_az - diger_xerc_az   + x4)
    y4_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az

    x5 = x4 * (1 + rental_growth_az / 100)
    y5_val_az = (y5_growth_az - diger_xerc_az   + x5)
    y5_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az

    x6 = x5 * (1 + rental_growth_az / 100)
    y6_val_az = (y6_growth_az - diger_xerc_az   + x6)
    y6_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az

    x7 = x6 * (1 + rental_growth_az / 100)
    y7_val_az = (y7_growth_az - diger_xerc_az   + x7)
    y7_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az

    x8 = x7 * (1 + rental_growth_az / 100)
    y8_val_az = (y8_growth_az - diger_xerc_az   + x8)
    y8_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az

    x9 = x8 * (1 + rental_growth_az / 100)
    y9_val_az = (y9_growth_az - diger_xerc_az   + x9)
    y9_yatirim_net_deyeri_az = amount  + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az

    x10 = x9 * (1 + rental_growth_az / 100)
    y10_val_az = (y10_growth_az - diger_xerc_az  - monthly_loan_az * 12 + x10)
    y10_yatirim_net_deyeri_az = amount + y1_val_az + y2_val_az + y3_val_az + y4_val_az + y5_val_az + y6_val_az + y7_val_az + y8_val_az + y9_val_az + y10_val_az
    dataaz2 = [round(y1_yatirim_net_deyeri_az, 0),
                       round(y2_yatirim_net_deyeri_az, 0),
                       round(y3_yatirim_net_deyeri_az, 0),
                      round(y4_yatirim_net_deyeri_az, 0),
                       round(y5_yatirim_net_deyeri_az, 0),
                       round(y6_yatirim_net_deyeri_az, 0)  ,
                      round(y7_yatirim_net_deyeri_az, 0),
                       round(y8_yatirim_net_deyeri_az, 0),
                       round(y9_yatirim_net_deyeri_az, 0),
                      round(y10_yatirim_net_deyeri_az, 0)]

    data['dataaz2'] = dataaz2[:year]


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


    data['field1'] = 120000

    data['year'] = year

    if year == 1:
        data['kiraye'] = round(kiraye1, 0)
        data['deyer'] = round(deyer_toplam1, 0)
    elif year == 2:
        data['kiraye'] = round(kiraye1 + kiraye2, 0)
        data['deyer'] = round(deyer_toplam2, 0)
    elif year == 3:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3, 0)
        data['deyer'] = round(deyer_toplam3, 0)
    elif year == 4:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4, 0)
        data['deyer'] = round(deyer_toplam4, 0)
    elif year == 5:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5, 0)
        data['deyer'] = round(deyer_toplam5, 0)
    elif year == 6:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6, 0)
        data['deyer'] = round(deyer_toplam6, 0)
    elif year == 7:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7, 0)
        data['deyer'] = round(deyer_toplam7, 0)
    elif year == 8:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8, 0)
        data['deyer'] = round(deyer_toplam8, 0)
    elif year == 9:
        data['kiraye'] = round(kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8 + kiraye9,
                               0)
        data['deyer'] = round(deyer_toplam9, 0)
    elif year == 10:
        data['kiraye'] = round(
            kiraye1 + kiraye2 + kiraye3 + kiraye4 + kiraye5 + kiraye6 + kiraye7 + kiraye8 + kiraye9 + kiraye10, 0)
        data['deyer'] = round(deyer_toplam10, 0)
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
        'is_mobile': is_mobile,
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
