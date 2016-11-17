"""
Write a recursive function (pseudocode and code) to check if
a number n is prime (hint: check whether n is divisible by
any number below n).
"""


def isprime(checknum, divisor):
    if divisor == checknum:
        return True
    elif checknum % divisor == 0:
        return False
    else:
        return isprime(checknum, divisor+1)

count = 2
answer = 0
number = int(input("Enter the number to check for primality"))




answer = isprime(number, count)
print(answer)
