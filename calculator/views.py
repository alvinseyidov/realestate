from django.shortcuts import render


def calculate_mortgage(loan_amount, years, interest_rate):
    # Convert loan amount to float
    loan_amount = float(loan_amount)

    # Convert years to months
    months = float(years) * 12

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = float(interest_rate) / 100 / 12

    # Formula to calculate monthly payments
    mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
                       ((1 + monthly_interest_rate) ** months - 1)

    # Return the monthly mortgage payment rounded to 2 decimal places
    return round(mortgage_payment, 2)


def calculate_yearly_increase(total_investment, appraisal_rate, years):
    # Convert appraisal rate to decimal
    appraisal_rate = appraisal_rate / 100
    # Initialize list to store the increase for each year
    yearly_increases = []
    # Start with total investment as the initial value
    current_value = total_investment

    # Loop through each year to calculate the increase
    for year in range(1, years + 1):
        # Calculate the value increase for the year
        increase = current_value * appraisal_rate
        # Append the increase to the list
        yearly_increases.append(increase)
        # Update the current value for the next year's calculation
        current_value += increase

    return yearly_increases




def calculate_yearly_value(total_investment, appraisal_rate, years):
    # Convert appraisal rate to decimal
    appraisal_rate = appraisal_rate / 100
    # Initialize list to store value for each year
    yearly_values = []
    # Start with total investment as the initial value
    current_value = total_investment

    # Loop through each year to calculate the value
    for year in range(1, years + 1):
        # Calculate value increase for the year
        current_value = current_value + (current_value * appraisal_rate)
        # Append the result to the list
        yearly_values.append(current_value)

    return yearly_values


def calculate_rental_income_yearly(total_investment, rental_income_coefficient, rental_growth, years):
    # Initialize list to store rental income for each year
    rental_income_yearly = []

    # Calculate rental income for the first year
    first_year_income = total_investment * rental_income_coefficient/100
    rental_income_yearly.append(first_year_income)

    # Loop through subsequent years to calculate the rental income with rental growth
    for year in range(1, years):
        next_year_income = rental_income_yearly[-1] * (1 + rental_growth / 100)
        rental_income_yearly.append(next_year_income)

    return rental_income_yearly


def calculate_rental_income_monthly(total_investment, rental_income_coefficient, rental_growth, years):
    # Initialize list to store monthly rental income for each year
    rental_income_monthly = []

    # Calculate rental income for the first year and convert it to monthly income
    first_year_income = (total_investment * rental_income_coefficient / 100) / 12
    rental_income_monthly.append(first_year_income)

    # Loop through subsequent years to calculate monthly rental income with rental growth
    for year in range(1, years):
        next_year_income = (rental_income_monthly[-1] * 12) * (1 + rental_growth / 100) / 12
        rental_income_monthly.append(next_year_income)

    return rental_income_monthly


def calculate_general_income_over_years(total_investment, loan_amount, appraisal_rate, rental_income_coefficient,
                                        rental_growth, years, repair_expense=600, life_insurance=120, loan_interest_rate=6 ):
    # Calculate monthly loan payment
    monthly_loan_payment = calculate_mortgage(loan_amount, years,loan_interest_rate)
    # Yearly loan payment
    loan_payment_yearly = 12 * monthly_loan_payment

    # Calculate yearly value increases
    yearly_increase_values = calculate_yearly_increase(total_investment, appraisal_rate, years)

    # Calculate rental income yearly
    rental_income_yearly = calculate_rental_income_yearly(total_investment, rental_income_coefficient, rental_growth,
                                                          years)

    # Initialize list to store general income for each year
    general_income_yearly = []

    # Loop through each year to calculate the general income
    for i in range(years):
        general_income = yearly_increase_values[i] - (repair_expense + life_insurance) - loan_payment_yearly + \
                         rental_income_yearly[i]
        general_income_yearly.append(general_income)

    return general_income_yearly


def calculate_monthly_return_amount(total_investment, rental_income_coefficient, rental_growth, years,
                                    repair_expense=600, life_insurance=120, loan_interest_rate=6,
                                    initial_capital_percentage=55.5):
    # If initial capital is not given, use 55.5% of total investment
    initial_capital = total_investment * initial_capital_percentage / 100
    # Calculate loan amount
    loan_amount = total_investment - initial_capital

    # Calculate monthly loan payment
    monthly_loan_payment = calculate_mortgage(loan_amount, years, loan_interest_rate)
    # Yearly loan payment
    yearly_loan_payment = 12 * monthly_loan_payment

    # Calculate rental income yearly
    rental_income_yearly = calculate_rental_income_yearly(total_investment, rental_income_coefficient, rental_growth,
                                                          years)

    # Calculate monthly return amount for each year
    monthly_return_amounts = []
    for i in range(years):
        yearly_return_amount = rental_income_yearly[i] - yearly_loan_payment - (life_insurance + repair_expense)
        monthly_return_amounts.append(yearly_return_amount / 12)  # Convert yearly return amount to monthly

    return monthly_return_amounts




def calculate_investment_net_value(total_investment, general_income, yearly_loan_payment, years, current_year):
    # Calculate the cumulative general income up to the current year
    cumulative_general_income = sum(general_income[:current_year])

    # Calculate the investment net value for the current year
    investment_net_value = total_investment - (yearly_loan_payment * (years - current_year)) + cumulative_general_income

    return investment_net_value

def calculate_investment_net_value_for_years(total_investment, general_income, yearly_loan_payment, years):
    # Calculate the investment net value for each year
    investment_net_values = []
    for year in range(1, years + 1):
        investment_net_value = calculate_investment_net_value(total_investment, general_income, yearly_loan_payment, years, year)
        investment_net_values.append(investment_net_value)
    return investment_net_values


def calculate_expected_investment_income(investment_net_value, initial_capital, total_investment, other_expenses=5):
    # Calculate other expenses as a percentage of the total investment
    expense_deduction = total_investment * (other_expenses / 100)
    # Calculate expected investment income (Net)
    expected_investment_income = investment_net_value - initial_capital - expense_deduction
    return expected_investment_income


# Example usage for 10 years, 90,000 total investment
def calculate_expected_investment_income_for_years(total_investment, general_income, yearly_loan_payment, years,
                                                   other_expenses=5):
    # Calculate initial capital (55.5% of total investment)
    initial_capital = total_investment * 55.5 / 100

    # Recalculate investment net values for each year
    investment_net_values = calculate_investment_net_value_for_years(total_investment, general_income,
                                                                     yearly_loan_payment, years)

    # Calculate expected investment income for each year
    expected_investment_income_yearly = [
        calculate_expected_investment_income(investment_net_value, initial_capital, total_investment, other_expenses)
        for investment_net_value in investment_net_values
    ]

    return expected_investment_income_yearly



# Function to calculate the profit margin percentage
def calculate_profit_margin_percent(expected_investment_income, initial_capital, total_investment, other_expense_percent=5):
    # Calculate other expenses
    other_expenses = total_investment * (other_expense_percent / 100)
    # Calculate profit margin percentage
    profit_margin_percent = (expected_investment_income / (initial_capital + other_expenses)) * 100
    return profit_margin_percent

# Example usage for all years
def calculate_profit_margin_for_all_years(expected_investment_income_list, initial_capital, total_investment, other_expense_percent=5):
    return [
        calculate_profit_margin_percent(expected_income, initial_capital, total_investment, other_expense_percent)
        for expected_income in expected_investment_income_list
    ]


def test(request):
    monthly_loan_payment = calculate_mortgage(40000,10, 6)
    yearly_increase = calculate_yearly_value(90000, 7.3, 10)
    yearly_value = calculate_yearly_increase(90000, 7.3, 10)
    rental_income_yearly = calculate_rental_income_yearly(180000,5.33,7.5, 5)
    general_incomes = calculate_general_income_over_years(90000, 40000,7.3,5.33,7.5,10)
    monthly_return_amount= calculate_monthly_return_amount(90000,5.33,7.5,10)
    investment_net_value = calculate_investment_net_value_for_years(90000,general_incomes, monthly_loan_payment*12, 10)
    expected_investment_income_for_years = calculate_expected_investment_income_for_years(90000,general_incomes, monthly_loan_payment*12, 10)
    profit_margin_for_all_years = calculate_profit_margin_for_all_years(expected_investment_income_for_years,50000,90000,)
    context = {
        "monthly_loan_payment":monthly_loan_payment,
        "yearly_increase":yearly_increase,
        "yearly_value":yearly_value,
        "rental_income_yearly":rental_income_yearly,
        "general_incomes":general_incomes,
        "monthly_return_amount":monthly_return_amount,
        "investment_net_value":investment_net_value,
        "expected_investment_income_for_years":expected_investment_income_for_years,
        "profit_margin_for_all_years":profit_margin_for_all_years,
    }
    return render(request, "test.html", context)


from django.http import JsonResponse


def calculate_investment_view(request):
    if request.method == 'GET':
        year = int(request.GET.get('year'))
        initial_capital = float(request.GET.get('amount'))

        # Calculate total investment based on initial capital
        total_investment = initial_capital / 0.555  # Initial capital is 55.5% of total investment
        loan_amount = total_investment - initial_capital  # Loan is the remainder of total investment

        # Perform the calculations (use the functions we created earlier)
        general_income = calculate_general_income_over_years(
            total_investment,
            loan_amount,  # Include loan amount here
            appraisal_rate=7.3,  # Adjust as needed
            rental_income_coefficient=5.33,
            rental_growth=7.5,
            years=year
        )

        yearly_loan_payment = 12 * calculate_mortgage(loan_amount, year, 6)  # Using correct loan amount
        investment_net_value = calculate_investment_net_value_for_years(
            total_investment, general_income, yearly_loan_payment, year
        )

        expected_investment_income = calculate_expected_investment_income_for_years(
            total_investment, general_income, yearly_loan_payment, year, other_expenses=5
        )
        profit_margin_percent = calculate_profit_margin_for_all_years(
            expected_investment_income, total_investment * 0.555, total_investment, other_expense_percent=5
        )

        rental_income_monthly = calculate_rental_income_monthly(
            total_investment,
            rental_income_coefficient=5.33,
            rental_growth=7.5,
            years=year
        )

        # Calculate monthly return amount
        monthly_return_amounts = calculate_monthly_return_amount(
            total_investment,  # Total investment
            rental_income_coefficient=5.33,  # Rental income coefficient
            rental_growth=7.5,  # Rental growth
            years=year,  # Number of years
            repair_expense=600,  # Repair expenses
            life_insurance=120,  # Life insurance
            loan_interest_rate=6,  # Loan interest rate
            initial_capital_percentage=55.5  # Initial capital percentage
        )
        monthly_loan_payment = calculate_mortgage(loan_amount, year, 6)
        monthly_loan_payments = [round(monthly_loan_payment, 0) for _ in range(year)]
        # Round values to zero decimal points
        rounded_rental_income_monthly = [round(value) for value in rental_income_monthly]
        rounded_monthly_return_amounts = [round(value) for value in monthly_return_amounts]
        rounded_general_income = [round(value) for value in general_income]
        rounded_investment_net_value = [round(value) for value in investment_net_value]
        rounded_expected_investment_income = [round(value) for value in expected_investment_income]
        rounded_profit_margin_percent = [round(value) for value in profit_margin_percent]
        rounded_expected_property_value = [round(value) for value in
                                           calculate_yearly_value(total_investment, 7.3, year)]

        # Return the values as a JSON response
        return JsonResponse({
            'monthly_loan_payments': monthly_loan_payments,  # Using calculated monthly return amounts
            'rental_income_monthly': rounded_rental_income_monthly,  # Using calculated monthly return amounts
            'monthly_return_amount': rounded_monthly_return_amounts,  # Using calculated monthly return amounts
            'general_income': rounded_general_income,  # Add general income
            'investment_net_value': rounded_investment_net_value,
            'expected_property_value': rounded_expected_property_value,
            'expected_investment_income': rounded_expected_investment_income,
            'profit_margin_percent': rounded_profit_margin_percent
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
