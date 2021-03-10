#price of house is $1M. if buyer has good credit, they need to putdown 10%
#otherwise they need to put down 20%. Print the down payment.

houseprice=100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * houseprice
else:
    down_payment = 0.2 * houseprice

print(f"Down payment: ${down_payment}")