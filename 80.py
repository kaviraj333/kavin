a=int(input())
l=[]
while a:
	rem=a%10
	if rem%2==1:
		l.append(rem)
	a=a//10
l.reverse()
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])
