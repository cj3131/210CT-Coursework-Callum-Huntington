""" 
Write the pseudocode for a function which returns the highest perfect square
which is less or equal to its parameter (a positive integer). Implement this
in a programming language of your choice.

First, we check if the given parameter is a square number. If it is not, we can
check if the next biggest number is a square number. This continues until we
reach a square number.

Checking for a square is done by multiplying two identical integers together,
beginning at 1*1 and incrementing from there.
"""

checknum = int(input("Enter the parameter, and the highest perfect square beneath it will be returned. "))
possibleSq = checknum
counter = 1
checkifsquare = True

while checkifsquare == True:
	#Multiplication of the two integers exeeds the number we are checking, possibleSq, and so cannot be a square number.
	#So decrement possibleSq to begin checking the next number
	if counter * counter > possibleSq:
		counter = 1
		possibleSq -= 1
	#Multiplication of two identical integers gives the number we are checking, so it is a square number
	if counter * counter == possibleSq:
		checkifsquare = False
		print("The highest perfect square up to and including ",checknum, "is ", possibleSq)
	#Multiplication of the two identical integers gives a number smaller than the number we are checking, so we can increment them
	if counter * counter < possibleSq:
		counter += 1
