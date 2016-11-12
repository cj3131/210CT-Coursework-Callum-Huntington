    def binarySearch(alist, item, lowbound, upperbound):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
    	midpoint = (first + last) // 2
        if alist[midpoint] == item:
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