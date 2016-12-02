"""
Q2: Count the number of trailing 0s in a factorial number. 


Terminates after a user has entered a number of which to find the factorial value, and it has been calculated.


The only valid input is a positive integer. Anything else will not be accepted.


Time complexity O(N). The factorial function is called once for each value of n.
"""

#The factorial function itself, returns n!
def factorial(n):
    if n == 0: #We have finished iterating down from the original number, so now close all the recursive calls.
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        factorialNum = int(input("Enter the value of n: "))
        if factorialNum < 0:
            raise ValueError
        break
    except:
        print("Invalid input. Enter a positive integer.")


numZeros = 0
counter = -1


print("The factorial number is ", factorial(factorialNum))

#Convert the factorial number from integer to string to be able to address values by index
factorialStr = str(factorial(factorialNum))


#Starting from the last index value of the string moving backwards, check the value in that position is "0"
#If it isn't, stop counting
for i in range(len(factorialStr), 0, -1):    
    if int(factorialStr[counter]) == 0: 
        numZeros += 1
        counter -= 1
    else:
        break


print("The number of trailing zeroes is ", numZeros)
