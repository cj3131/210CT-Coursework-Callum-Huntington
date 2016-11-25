"""
Given a sequence of n integer numbers, extract the sub-sequence of
maximum length which is in ascending order.
"""
numList = [3,4,7,2,9,6,1,9,13,16,18,20,25]
finalList = []
tempList = []
bestSeqLength = 0

for i in numList:
    #if the next number in the list is larger than the last item in the potential sequence, add it to the sequence
    if tempList == [] or i >= tempList[-1]:
        tempList.append(i)
    #if the current potential sequence is longer than the current best sequence, replace the best sequence.
    if bestSeqLength <= len(tempList):
        finalList = tempList
        bestSeqLength = len(finalList)
        print("Best so far: ", finalList)
    #if the sequence is broken, start a new potential sequence. 
    if i < tempList[-1]:
        tempList = []


print("The best sequence is ",  finalList, " of length ", bestSeqLength)
