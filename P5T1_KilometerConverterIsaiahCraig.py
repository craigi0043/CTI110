# Converts kilometers to miles
# 9/26/2018
# CTI-110 P5T1_KilometerConverter
# Isaiah Craig
#

# Set the conversion factor.
conversion_factor = 0.6214

def main():
    # Get the distance in kilometers.
    km = float(input('Enter the distance in kilometers:'))

    # Display the distance converted to miles
    show_miles(km)


def show_miles(km):
    # Calculate miles
    miles = km * conversion_factor

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles')


main()
