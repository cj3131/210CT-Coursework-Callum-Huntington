"""
Write a recursive function (pseudocode and code) to check if
a number n is prime (hint: check whether n is divisible by
any number below n).

Pseudocode:

IS_PRIME(checkNum, divisor)
	if divisor = checkNum
		return True
	else if (checkNum % divisor) = 0
		return False
	else return IS_PRIME(checkNum, divisor + 1)

print IS_PRIME(number, divider)

"""

# Checks if a number is prime by incrementing a divisor by 1 until it is equal to the checked number. If a number 
# ever divides into the checked number, it cannot be a prime number. 
def isprime(checknum, divisor):
    if divisor == checknum:
        return True
    elif checknum % divisor == 0:
        return False
    else:
        return isprime(checknum, divisor+1)

count = 2
answer = 0
while True:
    try:
        number = int(input("Enter the number to check for primality"))
        break
    except:
        print("Enter a valid integer.")




answer = isprime(number, count)
print(answer)
