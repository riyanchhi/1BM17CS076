import sys
n=int(input("Enter the number:"))
list=[]
def printDivisors(n) : 
    i = 1
    while i <= n : 
        if (n % i==0) : 
            list.append(i) 
        i = i + 1
    print(list)
          
# Driver program to test above function 
print("The divisors are:") 
printDivisors(n) 
     
 
