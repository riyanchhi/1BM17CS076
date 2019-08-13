#fibonacci series
import sys
n=int(input())
list = [0,1]
for i in range(2,n):
    list.append(list[i-1]+list[i-2])
print(list)    
