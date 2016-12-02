"""
Q7: Write a recursive function (pseudocode and code) to check if
a number n is prime (hint: check whether n is divisible by
any number below n).


This program terminates when the user has entered a valid input and the isprime function has returned
an answer of True or False.


The only valid input is a number larger than 1. All negative numbers are not prime numbers and 0 does
not meet the definition of a prime number: it must be greater than one. If the user tries to enter
these values they will receive a message telling them this.


The number is tested by trying to divide 2 into it. If this doesn't give a whole number, try dividing
3 into it. We continue incrementing like this until the divisor is the same as the tested number,
at which point we can conclude that no number other than itself or 1 can divide into it so it is prime. 


Pseudocode:


IS_PRIME(checkNum, divisor)
    if divisor = checkNum
        return True
    else if (checkNum % divisor) = 0
        return False
    else return IS_PRIME(checkNum, divisor + 1)


print IS_PRIME(number, divider)


"""


#Checks if a number is prime by incrementing a divisor by 1 until it is equal to the checked number. If a number 
#ever divides into the checked number, it cannot be a prime number. 
def isprime(checknum, divisor):
    if divisor == checknum:
        return True
    elif checknum % divisor == 0:
        return False
    else:
        return isprime(checknum, divisor+1)


count = 2
while True:
    try:
        number = int(input("Enter the number to check for primality"))
        if number == 0:
            print("0 is not a prime number. Try another number.")
            continue
        elif number == 1:
            print("1 is a prime number. Try another number.")
            continue
        elif number < 0:
            print("No negative number can be prime. Try another number.")
            continue
        break
    except:
        print("Enter a valid integer.")

if isprime(number, count) == True:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
