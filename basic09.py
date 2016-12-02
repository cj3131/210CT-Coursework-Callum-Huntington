"""
Adapt the binary search algorithm so that instead of outputting whether
a specific value was found, it outputs whether a value within an
interval (specified by you) was found.
Write the pseudocode and code and give the time complexity of the
algorithm using the Big O notation.
Example input:  L = [2,3,5,7,9,13]   low= 10   high = 14   Output: True

Pseudocode:

def BINARY_SEARCH(list, lowerBound, upperBound):
    while listStart <= listEnd and found = False:
        listMiddle <-- (listStart + listEnd) / 2
        if list[listMiddle] >= lowerBound or list[listMiddle] <= upperBound:
            found 

Time complexity of O(log(n)) since the list is constantly being made half it's previous size with each iteration.
"""
def binarySearch(alist, lowbound, upperbound):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2 # The midpoint will always be the value of the list's middle element's index 
        if alist[midpoint] >= lowbound and alist[midpoint] <= upperbound:
            found = True
        else:
            #if the boundary of numbers are smaller than the current midpoint, ignore the second half of the list
            if upperbound < alist[midpoint]:
                last = midpoint-1
            #the boundary of numbers must be larger than the current midpoint so ignore the first half of the list
            else:
                first = midpoint+1
 
    return found

while True:
    try:
        low = int(input("Enter the lower boundary"))
        break
    except:
        print("Invalid input. Enter the lower boundary")

while True:
    try:
        high = int(input("Enter the upper boundary"))
        break
    except:
        print("Invalid input. Enter the upper boundary")




testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, low, high))