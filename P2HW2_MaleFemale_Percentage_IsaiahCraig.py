# A brief description of the project
# 9/5/2018
# CTI-110 P2HW2 - Male Female Percentage
# Isaiah Craig
#
# Get the total number of males and females.
total = float(input('Enter the total amount of people: '))

# Get the total numbe of males.
males = float(input('Enter the total number of males: '))

# Get the total number of females.
females= float(input('Enter the total number of females: '))

# Calculate the percentage of males.
malespercent= males / total

# Calculate the percentage of females.
femalespercent= females / total

# Display the percentages
print('The percentage of males is', format(malespercent, '%'))
print('The percentage of females is', format(femalespercent, '%'))
