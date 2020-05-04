def insertion_sort(data):
    for i in range (1 , len(data)):
        temp = data[i]
        j=i-1

        while j>=0 and data[j] >temp:
            data[j+1] = data[j]
            j-=1

        data[j+1] = temp

arr = [5,3,1,8,7,2,4]
insertion_sort(arr)

for i in range (len(arr)):
  print(arr[i])
