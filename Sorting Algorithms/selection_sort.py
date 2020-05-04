def selection_sort(data):
    for i in range (0, len(data)):
        
        least = i
        j=i+1

        while j<len(data):
            
            if(data[j] < data[least]):
                least = j                #find the least item
                
            j+=1
            
             #swap
            temp = data[i]              
            data[i] = data[least]
            data[least]=temp
            
            
arr = [5,3,1,8,7,2,4]
selection_sort(arr)

for i in range (len(arr)):
  print(arr[i])
        
