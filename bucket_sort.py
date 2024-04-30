import random
import time


def bucket_sort(arr):
  buckets = [[] for _ in range(len(arr))]
  for num in arr:
    index = int(num * len(arr))
    buckets[index].append(num)
  sorted_arr = []
  for bucket in buckets:
    sorted_arr.extend(sorted(bucket))
  return sorted_arr


number = int(input())
my_list = list(range(number))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
bucket_sort(my_list)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
