

#Named constants to represent the quanitity multiplier.

DISCOUNT1 = 0.10
DISCOUNT2 = 0.20
DISCOUNT5 = 0.30
DISCOUNT100 = 0.40

PRICE = 99.0

TOTAL1= PRICE - DISCOUNT1
TOTAL2 = PRICE - DISCOUNT2
TOTAL5 = PRICE - DISCOUNT5
TOTAL100 = PRICE - DISCOUNT100

#Get the total number of packages purchased.

quantity =int(input('Enter the quantity of packages to purchase: '))

#Calcuate the discount.
#Display the discount amount.


if quantity >=10 and quantity <=19:
    tprice=float(PRICE * quantity)
    tdisc=float(tprice*DISCOUNT1)

    print('The total price before discount is: \t$'+ format(tprice,',.2f'))
    print('The total discount is: \t$'+ format(tdisc,',.2f'))
    print('The final cost is: \t$'+ format(tprice - tdisc,',.2f'))
    
elif quantity >=20 and quantity <=49:
    tprice=float(PRICE * quantity)
    tdisc=float(tprice*DISCOUNT2)
    print('The total price before discount is: \t$'+ format(tprice,',.2f'))
    print('The total discount is: \t$'+ format(tdisc,',.2f'))
    print('The final cost is: \t$'+ format(tprice - tdisc,',.2f'))

elif quantity >=50 and quantity <=99:
    tprice=float(PRICE * quantity)
    tdisc=float(tprice*DISCOUNT5)
    print('The total price before discount is: \t$'+ format(tprice,',.2f'))
    print('The total discount is: \t$'+ format(tdisc,',.2f'))
    print('The final cost is: \t$'+ format(tprice - tdisc,',.2f'))

elif quantity >= 100 and quantity <= 5000:
    tprice=float(PRICE * quantity)
    tdisc=float(tprice*DISCOUNT100)
    print('The total price before discount is: \t$'+ format(tprice,',.2f'))
    print('The total discount is: \t$'+ format(tdisc,',.2f'))
    print('The final cost is: \t$'+ format(tprice - tdisc,',.2f'))

elif quantity >5001:
    print('Exceeded quantity limit. ')

else:
    
    print('Your total is ', format(quantity * PRICE, ',.2f'))
