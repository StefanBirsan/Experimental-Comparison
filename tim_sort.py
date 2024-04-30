import random
import time


def gallop(arr, start, end, key):

  while start < end:
    mid = (start + end) // 2
    if arr[mid] < key:
      start = mid + 1
    else:
      end = mid
  return start

def merge(arr, left, mid, right):
 
  n1 = mid - left + 1
  n2 = right - mid

  L = arr[left:mid + 1]
  R = arr[mid + 1:right + 1]

  i = 0
  j = 0
  k = left
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  
  while i < n1:
    arr[k] = L[i]
    i += 1
  while j < n2:
    arr[k] = R[j]
    j += 1

def timsort(arr):
 
  min_run = 32  
  n = len(arr)

  for i in range(0, n, min_run):
    insertion_sort(arr, i, min((i + min_run - 1, n - 1)))

  size = min_run
  while size < n:
    for start in range(0, n, size * 2):
      mid = min(start + size - 1, n - 1)
      end = min((start + size * 2 - 1, (n - 1)))
      end = gallop(arr, mid + 1, end, arr[mid])
      merge(arr, start, mid, end)
    size *= 2

def insertion_sort(arr, left, right):

  for i in range(left + 1, right + 1):
    key = arr[i]
    j = i - 1
    while j >= left and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

number = int(input())
my_list = list(range(number))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
timsort(my_list)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
