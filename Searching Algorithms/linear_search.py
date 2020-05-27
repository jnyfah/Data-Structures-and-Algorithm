def linearsearch(data, key):
	n = False

	for i in range (len(data)):
		if data[i] == key:
			n = True
	if n == True:
		print("found")
	else:
		print("not found")


arr = [5,3,1,8,7,2,4]
linearsearch(arr, 3)

