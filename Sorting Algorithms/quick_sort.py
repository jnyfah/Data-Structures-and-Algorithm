import random

def quicksort(data):
	n = len(data)
	quick(data, 0, n-1)


def quick (data, first, last):

	if first >= last:
		return
	else:
		#n = len(data)
		#index = random.randint(1, n-1) 
		pivot = data[first]

		pos = partition (data, first, last)

		quick(data, first, pos)
		quick(data, pos +1, last)


def partition(data, first, last):
	
	#n = len(data)
	#index = random.randint(1, n-1) 
	pivot = data[first]

	left = first +1
	right = last

	while left <=right :
		while left < right and data[left] < pivot:
			left +=1

		while right>=left and data[right] >= pivot:
			right -=1

		if left < right:
			temp = data[left]
			data[left] = data[right]
			data[right] = temp

		if right != first:
			data[first] = data[right]
			data[right] = pivot

		return right


arr = [5,3,1,8,7,2,4]
quicksort(arr)

for i in range (len(arr)):
  print(arr[i])
