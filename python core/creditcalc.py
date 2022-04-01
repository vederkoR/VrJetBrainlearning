import argparse
import math


def monthly_payment_calc(_loan_principal, _monthly_payment, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    period_months = math.log(_monthly_payment /
                             (_monthly_payment - interest_rate * _loan_principal), 1 + interest_rate)
    return period_months


def loan_principle_calc(_annuity_payment, _number_of_periods, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    line1 = interest_rate * math.pow((1 + interest_rate), _number_of_periods)
    line2 = math.pow((1 + interest_rate), _number_of_periods) - 1
    line3 = line1 / line2
    _loan_principal = _annuity_payment / line3
    return int(_loan_principal)  # int(math.ceil())


def annuity_payment_calc(_loan_principal, _number_of_periods, _loan_interest):
    interest_rate = _loan_interest / (12 * 100)
    line1 = interest_rate * math.pow((1 + interest_rate), _number_of_periods)
    line2 = math.pow((1 + interest_rate), _number_of_periods) - 1
    _annuity_payment = _loan_principal * line1 / line2
    return int(math.ceil(_annuity_payment))


def differentiated_payment_calc(_loan_principal, _number_of_periods, _loan_interest):
    amount = 0
    for m_ in range(1, (_number_of_periods + 1)):
        interest_rate = _loan_interest / (12 * 100)
        differentiated_payment__ = (_loan_principal / _number_of_periods) + interest_rate * \
                                   (_loan_principal - (_loan_principal * (m_ - 1) / _number_of_periods))
        amount_ceiled = math.ceil(differentiated_payment__)
        print(f"Month {m_}: payment is {amount_ceiled}")
        amount += amount_ceiled
    print()
    print(f"Overpayment = {int(amount - _loan_principal)}")


def period_output():
    global period
    if period == 1:
        print('It will take 1 month to repay the loan')
    elif period == 12:
        print('It will take 1 year to repay the loan')
    elif period % 12 == 0:
        period_y = period / 12
        print(f'It will take {int(period_y)} years to repay the loan')
    elif period < 12:
        print(f'It will take {int(period)} months to repay the loan')
    else:
        y = period // 12
        m = period % 12
        if y == 1 and m == 1:
            print("It will take 1 year and 1 month to repay this loan!")
        elif y == 1:
            print(f"It will take 1 year and {int(m)} months to repay this loan!")
        elif m == 1:
            print(f"It will take {int(y)} years and 1 month to repay this loan!")
        else:
            print(f"It will take {int(y)} years and {int(m)} months to repay this loan!")


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"], help="mode of calculation")
parser.add_argument("--payment", help=" the monthly payment amount")
parser.add_argument("--principal", help="loan principal")
parser.add_argument("--periods", help="denotes the number of months needed to repay the loan")
parser.add_argument("--interest", help="nominal interest rate. This is usually 1/12 of the annual interest rate")
args = parser.parse_args()

try:
    if args.type == "diff":
        loan_principal = float(args.principal)
        number_of_periods = int(args.periods)
        loan_interest = float(args.interest)
        differentiated_payment_calc(loan_principal, number_of_periods, loan_interest)
        if loan_principal < 0 or number_of_periods < 0 or loan_interest < 0:
            raise Exception()

    elif args.type == "annuity":
        if args.periods is None:
            loan_principal = float(args.principal)
            monthly_payment = int(args.payment)
            loan_interest = float(args.interest)
            if loan_principal < 0 or monthly_payment < 0 or loan_interest < 0:
                raise Exception()

            period = int(math.ceil(monthly_payment_calc(loan_principal, monthly_payment, loan_interest)))
            period_output()
            print(f"Overpayment = {int(monthly_payment * period - loan_principal)}")
        elif args.principal is None:
            annuity_payment = float(args.payment)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            if annuity_payment < 0 or number_of_periods < 0 or loan_interest < 0:
                raise Exception()

            loan_principal = loan_principle_calc(annuity_payment, number_of_periods, loan_interest)
            print(f'Your loan principal = {loan_principal}!')
            print(f"Overpayment = {int(annuity_payment * number_of_periods - loan_principal)}")
        elif args.payment is None:
            loan_principal = float(args.principal)
            number_of_periods = int(args.periods)
            loan_interest = float(args.interest)
            if loan_principal < 0 or number_of_periods < 0 or loan_interest < 0:
                raise Exception()

            annuity_payment = annuity_payment_calc(loan_principal, number_of_periods, loan_interest)
            print(f'Your monthly payment = {annuity_payment}!')
            print(f"Overpayment = {int(annuity_payment * number_of_periods - loan_principal)}")
finally:
    print("Incorrect parameters")
