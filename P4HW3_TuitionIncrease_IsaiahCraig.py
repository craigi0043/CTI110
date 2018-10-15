# Display the projected smester tuition amount for the next 5 years
# 9/24/2018
# CTI-110 P4HW3 - Tuition Increase
# Isaiah Craig
#

# Set accumulator
tuition = 8000

# Header
print ('Tuition Increase for the next 5 years:')

# Calculate tuition
for year in range(1, 6):
    tuition = tuition + ( .03 ) * tuition
    print("Year", year, "\t", "$", format(tuition, '.2f'))
