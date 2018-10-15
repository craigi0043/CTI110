# Converts feet to inches
# 9/26/2018
# CTI-110 P5T2_FeetToInches
# Isaiah Craig
#

# Set constant
inchesperfoot = 12

# Main function
def main():
    # Get the number of feet.
    feet = int(input('Enter the number of feet: '))

    # Convert feet to inches.
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# Feet to inches function.
def feet_to_inches(feet):
    return feet * inchesperfoot

main()
