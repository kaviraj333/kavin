class roundit:
	def todecimal(self,n):
		if((n % 1) > 0.5):
			n1=round(n)
			print(n1)
		else:
			n1=round(n)
			print(n1+1)
n=input()
call=roundit()
call.todecimal(float(n))
