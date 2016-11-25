"""
Count the number of trailing 0s in a factorial number. 

Time complexity O(N). The factorial function is called once for each value of n.
"""

#The factorial function itself, returns !n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorialNum = int(input("Enter the value of n: "))
numZeros = 0
counter = -1

print("The factorial number is ",factorial(factorialNum))

#Convert the factorial number from integer to string to be able to address values by index
factorialStr = str(factorial(factorialNum))

#Starting from the last index value of the string moving backwards, check the value in that position is equal to 0
#If it isn't, stop counting

for i in range(len(factorialStr),0,-1):    
    if int(factorialStr[counter]) == 0: 
        numZeros += 1
        counter -= 1
    else:
        break

print("The number of trailing zeroes is ", numZeros)