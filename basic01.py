"""
Write a function that randomly shuffles an array of integers and explain
the rationale behind its implementation. 

This program won't terminate until the user enters "n". As soon
as they do, the new list will be created and the program will end.

The algorithm will crash if the input is negative or a non-integer value other than "n".

Time complexity of O(N). The for loop will execute as many times as there are items in the list.
"""

import random
randomPosition = 0
newList = []
removedNum = 0

#Collect the list of integers
numberList = [int(input("Input the first number in the list"))]
nextNum = input("Enter the next number of the list, or input n to stop and shuffle")

while nextNum != "n":
    numberList.append(int(nextNum))
    nextNum = input("Enter the next number of the list, or input n to stop and shuffle")
print("The old list was:  ", numberList)

#It is generally a bad idea to change the value of a condition that
#is being looped through, so create two listLengths.
listLengthLoop = len(numberList)
listLength = len(numberList)

#Remove an element from the old list n times, where n is the length of the old list
#Remove an element from the old list at the randomly selected index value
#and place it in the next available space in the new list.
for i in range(listLengthLoop):
    randomPosition = random.randint(0,listLength-1)
    removedNum = numberList.pop(randomPosition)
    newList.append(removedNum)
    listLength = len(numberList)
print("The new, shuffled list is:  ",newList)
