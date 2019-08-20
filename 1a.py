def fun(arr,n):
	b=[]
	print("Even number in the list")
	for i in arr:
		if i%2==0:
			b.append(i)
	print(b)
arr=[]
n=int(input("Enter size"))
print("enter the list")
for x in range(n):
	item=int(input())
	arr.append(item)
print("Given list:",str(arr))
fun(arr,n)
