import time
import random
import sys

#recursion function for bubble sort
def BubbleSort(arr, n):
    if (n > 0):
        for i in range(0, n):
            if (arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        BubbleSort(arr, n - 1)

#to set custom recursion stack value
sys.setrecursionlimit(10**6)

arr = []
n = int(input("Enter the size of the array: "))

# starting time
start = time.time()

print("Enter the Element of the array:")
for i in range(0, n):
    num = random.randint(0, n)
    arr.append(num)

BubbleSort(arr, n - 1)
print("After Sorting Array Elements are:")
for i in range(0, n):
    print(arr[i], end=" ")
    
#ending time
end = time.time()
# total time taken
print(f"runtime of the program is{end - start}")
