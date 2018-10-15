# Convert numbers to Roman Numerals.
# 9/10/2018
# CTI-110 P3HW1 - Roman Numerals
# Isaiah Craig
#
# Input a number.
number = int(input('Enter a number 1-10: '))

#Determine if the number is in range.
if number > 10:
    print('Error, This number is out of range.')
if number == 1:
    print('The Roman Numeral for 1 is I')
if number == 2:
    print('The Roman Numeral for 2 is II')
if number == 3:
    print('The Roman Numeral for 3 is III')
if number == 4:
    print('The Roman Numeral for 4 is IV')
if number == 5:
    print('The Roman Numeral for 5 is V')
if number == 6:
    print('The Roman Numeral for 6 is VI')
if number == 7:
    print('The Roman Numeral for 7 is VII')
if number == 8:
    print('The Roman Numeral for 8 is VIII')
if number == 9:
    print('The Roman Numeral for 9 is IX')
if number == 10:
    print('The Roman Numeral for 10 is X')
