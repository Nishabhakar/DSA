#bubble sort function
def bubbleSort(arr,n):
    if(n>0):
        for i in range(0,n):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        bubbleSort(arr, n - 1)

#main fuctin
arr=[]
n = int(input("Enter the size of ur array: "))
print("Enter the Element of  array:")
for i in range(0,n):
    num = int(input())
    arr.append(num)
bubbleSort(arr, n - 1) #bubblesorrt function called!
print("After Sorting Array Elements are:")
for i in range(0,n):
    print(arr[i],end=" ")