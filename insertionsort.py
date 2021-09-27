import random
import time

#insertion sort function
def insertionSort(arr):
    # Traverse through 1 to len(arr)

    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are

        # greater than key, to one position ahead

        # of their current position

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key



#main program
arr = []
n = int(input("Enter the size of the array: "))
# starting time
print("Enter the Element of the array:")
for i in range(0, n):
    num = random.randint(0, n)
    arr.append(num)

#starting time
start = time.time()

#callin insertion sort functyion
insertionSort(arr)

print("Sorted array is:")

for i in range(len(arr)):
    print("%d" % arr[i])

#ending time
end = time.time()
# total time taken
print(f"runtime of the program is{end - start}")
