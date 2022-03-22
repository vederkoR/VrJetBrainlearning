import math


def monthly_payment_calc(_loan_principal, _monthly_payment, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    period_months = math.log(_monthly_payment / (_monthly_payment - interest_rate * _loan_principal), 1 + interest_rate)
    return period_months


def loan_principle_calc(_annuity_payment, _number_of_periods, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    line1 = interest_rate * math.pow((1 + interest_rate), _number_of_periods)
    line2 = math.pow((1 + interest_rate), _number_of_periods) - 1
    line3 = line1 / line2
    _loan_principal = _annuity_payment / line3
    return int(math.ceil(_loan_principal))


def annuity_payment_calc(_loan_principal, _number_of_periods, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    line1 = interest_rate * math.pow((1 + interest_rate), _number_of_periods)
    line2 = math.pow((1 + interest_rate), _number_of_periods) - 1
    _annuity_payment = _loan_principal * line1 / line2
    return int(math.ceil(_annuity_payment))


# write your code here
print("What do you want to calculate?")
print('''type "n" - for number of monthly payments,
type "a" - for annuity monthly payment amount,
type "p" - for the monthly payment:''')
type_ = input()
if type_ == 'n':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    period = int(math.ceil(monthly_payment_calc(loan_principal, monthly_payment, loan_interest)))
    if period == 1:
        print('It will take 1 month to repay the loan')
    elif period == 12:
        print('It will take 1 year to repay the loan')
    elif period % 12 == 0:
        period /= 12
        print(f'It will take {period} years to repay the loan')
    elif period <12:
        print(f'It will take {period} months to repay the loan')
    else:
        y = period // 12
        m = period % 12
        if y == 1 and m == 1:
            print("It will take 1 year and 1 month to repay this loan!")
        elif y == 1:
            print(f"It will take 1 year and {m} months to repay this loan!")
        elif m == 1:
            print(f"It will take {y} years and 1 month to repay this loan!")
        else:
            print(f"It will take {y} years and {m} months to repay this loan!")
elif type_ == 'p':
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    number_of_periods = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    loan_principal = loan_principle_calc(annuity_payment, number_of_periods, loan_interest)
    print(f'Your loan principal = {loan_principal}!')
else:
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the number of periods:")
    number_of_periods = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    annuity_payment = annuity_payment_calc(loan_principal, number_of_periods, loan_interest)
    print(f'Your monthly payment = {annuity_payment}!')
