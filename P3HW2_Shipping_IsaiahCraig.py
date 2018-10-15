# CTI-110
# P3HW2 - Shipping Charges
# Isaiah Craig
# 9/11/2018
#
# Determine amount of pounds.
pounds = float(input('Enter how many pounds you item is: '))

# Calculate the pounds and cost.
if pounds <= 2:
    twoless = pounds * 1.50
    print('The shipping cost is $', format(twoless, ',.2f'))
if pounds > 2 and pounds <= 6:
    twotosix = pounds * 3.00
    print('The shipping cost is $', format(twotosix, ',.2f'))
if pounds > 6 and pounds <= 10:
    sixtoten = pounds * 4.00
    print('The shipping cost is $', format(sixtoten, ',.2f'))
if pounds > 10:
    ten = pounds * 4.75
    print('The shipping cost is $', format(ten, ',.2f'))
