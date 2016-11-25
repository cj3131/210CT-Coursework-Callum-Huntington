""" 
Write the pseudocode for a function which returns the highest perfect square
which is less or equal to its parameter (a positive integer). Implement this
in a programming language of your choice.

First, we check if the given parameter is a square number. If it is not, we can
check if the next biggest number is a square number. This continues until we
reach a square number.

Checking for a square is done by multiplying two identical integers together,
beginning at 1*1 and incrementing from there.


Pseudocode:

def CHECK_SQUARE(n):
	possSq <-- n
	counter <-- 1
	if counter * counter > possSq:
		counter <-- 1
		possSq <-- possSq - 1
	if counter * counter == possSq:
		print possSq
		end
	if counter * counter < possSq:
		counter <-- counter + 1


Time complexity of O(N). The larger N is, the more numbers might need to be checked as squares.
"""

checknum = int(input("Enter the parameter, and the highest perfect square beneath it will be returned. "))
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
		print("The highest perfect square up to and including ", checknum, "is ", possibleSq)
		break
	#Multiplication of the two identical integers gives a number smaller than the number we are checking, so we can increment them
	if counter * counter < possibleSq:
		counter += 1