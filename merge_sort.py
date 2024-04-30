import random
import time


def merge(arr, left, mid, right):

  n1 = mid - left + 1
  n2 = right - mid

  L = [0] * n1
  R = [0] * n2

  for i in range(0, n1):
    L[i] = arr[left + i]
  for j in range(0, n2):
    R[j] = arr[mid + 1 + j]

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


def mergeSort(arr, left, right):

  if left < right:
    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    merge(arr, left, mid, right)


number = int(input())
my_list = list(range(number))
random.shuffle(my_list)

print("Original list:", my_list)

start_time = time.time()
mergeSort(my_list, 0, len(my_list) - 1)
end_time = time.time()

total_time = (end_time - start_time) * 1000

print("Sorted list:", my_list)
print(f"Sorting time: {total_time:.5f} ms")
