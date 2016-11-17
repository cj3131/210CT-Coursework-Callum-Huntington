"""
Adapt the binary search algorithm so that instead of outputting whether
a specific value was found, it outputs whether a value within an
interval (specified by you) was found.
Write the pseudocode and code and give the time complexity of the
algorithm using the Big O notation.
Example input:  L = [2,3,5,7,9,13]   low= 10   high = 14   Output: True
"""
def binarySearch(alist, item, lowbound, upperbound):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
    	midpoint = (first + last) // 2
        if alist[midpoint] >= lowbound or alist[midpoint] <= upperbound:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
 
    return found


low = int(input("Enter the lower boundary"))
high = int(input("Enter the upper boundary"))


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3, low, high))
print(binarySearch(testlist, 13, low, high))