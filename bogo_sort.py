import random
import time


def is_sorted(arr):

  for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
      return False
  return True


def bogosort(arr):

  while not is_sorted(arr):
    random.shuffle(arr)


number = int(input())
my_list = list(range(number))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
bogosort(my_list)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
