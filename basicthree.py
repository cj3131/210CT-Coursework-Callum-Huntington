checknum = int(input("Enter the parameter, and the highest perfect square beneath it will be returned. "))
x = checknum
count = 1
checkifsquare = True

while checkifsquare == True:
	if count * count > x:
		count = 1
		x -= 1
	if count * count == x:
		checkifsquare = False
		print("The highest perfect square up to and including ",checknum, "is ", x)
	if count * count < x:
		count += 1
