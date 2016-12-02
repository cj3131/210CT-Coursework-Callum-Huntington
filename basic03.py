""" 
Q3: Write the pseudocode for a function which returns the highest perfect square
which is less or equal to its parameter (a positive integer). Implement this
in a programming language of your choice.


First, we check if the given parameter is a square number. If it is not, we can
check if the next biggest number is a square number. This continues until we
reach a square number.


Checking for a square is done by multiplying two identical integers together,
beginning at 1*1 and incrementing from there.


This program will terminate when the user has entered a valid integer and the largest perfect square number has been calculated.


The only valid input is a number greater than 0, since there cannot be a negative square number. 


Pseudocode:


CHECK_SQUARE(n)
    possSq <-- n
    counter <-- 1
    while found = False:
        if counter * counter > possSq
            counter <-- 1
            possSq <-- possSq - 1
        if counter * counter == possSq
            print possSq
            found <-- True
        if counter * counter < possSq
            counter <-- counter + 1




Time complexity of O(N). The larger N is, the more numbers might need to be checked as squares.
"""


while True:
    try:
        checknum = int(input("Enter the parameter, and the highest perfect square beneath it will be returned. "))
        if checknum == 0:
            print("The largest square number less than or equal to 0 is 0. Try another number.")
            continue
        if checknum < 0:
            raise ValueError
        break
    except:
            print("Invalid input. Enter a positive integer.")


possibleSq = checknum
counter = 1


while True:
    #Multiplication of the two integers exeeds the number we are checking, possibleSq, and so cannot be a square number.
    #So decrement possibleSq to begin checking the next number
    if counter * counter > possibleSq:
        counter = 1
        possibleSq -= 1
    #Multiplication of two identical integers gives the number we are checking, so it is a square number
    if counter * counter == possibleSq:
        print("The highest perfect square up to and including ", checknum, "is ", possibleSq, "\nIt's square root is ", counter)
        break
    #Multiplication of the two identical integers gives a number smaller than the number we are checking, so we can increment them
    if counter * counter < possibleSq:
        counter += 1
