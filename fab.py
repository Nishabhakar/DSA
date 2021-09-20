import time

#program body
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms =  int(input("Enter the value of 'n': "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")

#starting time
   start = time.time()

   for i in range(nterms):
       print(recur_fibo(i))

   end = time.time()

#total time taken
print(f"runtime of the program is{end - start}")
