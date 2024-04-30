import random
import time


def bubble_sort(arr):

  n = len(arr)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]


number = int(input())
my_list = list(range(number))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
bubble_sort(my_list)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
