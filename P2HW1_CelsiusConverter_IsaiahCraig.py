# Convert temperature from Celsius to Fahrenheit
# 9/5/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter
# Isaiah Craig
#
temperature = float(input('Enter the tempreature in Celsius: '))

#Calculate the temperature in Celsius to Fahrenheit
temperature2 = 9/5 * temperature + 32

#Display the Temperature in Fahrenheit
print('The temperature in Fahrenheit is', format(temperature2, ',.2f'))
