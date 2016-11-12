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
