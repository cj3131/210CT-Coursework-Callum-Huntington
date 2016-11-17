"""
Given a sequence of n integer numbers, extract the sub-sequence of
maximum length which is in ascending order.
"""
numlist = [3,4,7,2,9,6,1,9,13,16,18,20,25]
finallist = []
templist = []
bestseqlength = 0

for i in numlist:
    if templist == [] or templist[-1] <= i:
        templist.append(i)
        print("Did one ", i)
    if bestseqlength <= len(templist):
        finallist = templist[:]
        bestseqlength = len(finallist)
        print(finallist)
    if i < templist[-1]:
        templist = []


print("The best sequence is ",  finallist, " of length ", bestseqlength)
