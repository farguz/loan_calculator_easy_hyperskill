# https://hyperskill.org/projects/90/stages/503/implement
# creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
import math
import argparse


def annuity(principal, payment, periods, interest):
    i = interest / (12 * 100)  # monthly rate
    if principal == 0:
        principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
        print('Your loan principal = {}!'.format(round(principal)))
    elif payment == 0:
        payment = principal * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)
        print('Your annuity payment = {}!'.format(math.ceil(payment)))
    elif periods == 0:
        periods = math.log(payment / (payment - i * principal), (1 + i))
        periods = math.ceil(periods)  # round to closest up (since the last month is less than the others)
        if periods < 12:
            print('It will take {} months to repay this loan!'.format(periods))
        elif periods % 12 == 0:
            print('It will take {} years to repay this loan!'.format(periods // 12))
        else:
            print('It will take {} years and {} months to repay this loan!'.format(periods // 12, periods % 12))
    else:
        print('Incorrect parameters.')
    overpayment = math.ceil(payment) * periods - principal
    print('\nOverpayment = {}'.format(int(overpayment)))


def diff(interest, principal, periods):
    i = interest / (12 * 100)  # monthly rate
    overpayment = - principal
    for current_month in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - principal * (current_month - 1) / periods))
        print('Month {}: payment is {}'.format(current_month, payment))
        overpayment += payment
    print('\nOverpayment = {}'.format(math.ceil(overpayment)))


parser = argparse.ArgumentParser()
parser.add_argument('--type', action="store", dest="type", default='', type=str)
parser.add_argument('--principal', action="store", dest="principal", default=0, type=float)
parser.add_argument('--payment', action="store", dest="payment", default=0, type=float)
parser.add_argument('--periods', action="store", dest="periods", default=0, type=int)
parser.add_argument('--interest', action="store", dest="interest", default=0, type=float)

args = parser.parse_args()
principal, payment, periods, interest = args.principal, args.payment, args.periods, args.interest

# quick check of start parameters/conditions. no negative, no less than 4 parameters
if [principal, payment, periods, interest].count(0) > 1:
    print('Incorrect parameters.')
elif min(principal, payment, periods, interest) < 0:
    print('Incorrect parameters.')
elif args.type == 'annuity':
    annuity(principal, payment, periods, interest)
elif args.type == 'diff':
    diff(interest, principal, periods)
else:
    print('Incorrect parameters.')
