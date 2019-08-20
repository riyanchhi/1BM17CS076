import sys
def search(lis,a):
	print(lis)
	if a in lis:
		return True
	else:
		return False
ls=[]
while True:
	n=int(input ("Enter the element"))
	if n!=-1:
		ls.append(n)
	else:
		break
b=int(input("Enter the element the element searched"))
print(search(ls,b))
