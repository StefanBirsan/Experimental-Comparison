import random
import time

def partition(arr, low, high):

  pivot = arr[high]  
  
  i = low - 1  

  for j in range(low, high):
    
    if arr[j] < pivot:
     
      i += 1
     
      arr[i], arr[j] = arr[j], arr[i]


  arr[i + 1], arr[high] = arr[high], arr[i + 1]

  return i + 1

def quickSort(arr, low, high):

  if low < high:
   
    pi = partition(arr, low, high)


    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)


my_list = list(range(10))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
quickSort(my_list, 0, len(my_list) - 1)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
