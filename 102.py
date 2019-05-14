lst=[]
class capitalise:
	def firstletter(self,x):
		for i in x:
			lst.append(i)
		for i in range(len(lst)):
			lst[0]=lst[0].upper()
			if lst[i]==" ":
				lst[i+1]=lst[i+1].upper()
		for i in range(len(lst)):
			print(lst[i],end="")
x=input()
call=capitalise()
call.firstletter(x)
