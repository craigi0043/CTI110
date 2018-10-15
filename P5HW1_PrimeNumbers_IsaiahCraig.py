# Determines whether a number is prime or not.
# 9/26/2018
# CTI-110 P5HW1 - Prime Numbers
# Isaiah Craig
#


def isPrime(userNumber):
    evenDivisions = 0
    if userNumber <= 1:
        return False
    for currentNumber in range(1, userNumber + 1):
        if userNumber % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

def main():
    userNumber = int(input('Enter a number: '))
    print()
    if isPrime(userNumber):
        print(userNumber, 'is a prime number')
    else:
        print(userNumber, 'is not a prime number')

main()
        
