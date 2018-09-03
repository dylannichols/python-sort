import random

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1] :
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min] :
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp

length = random.randint(1, 30)
array = [10, 7]
for i in range(1, length) :
    array.append(random.randint(1, 100))
selectionSort(array)
for i in range(len(array)):
    print("%d" %array[i])