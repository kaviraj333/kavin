class summit:
	def of digit(self,n):
		count=0
		while(n>0):
			dig=n%10
			count+=dig
			n=n//10
		print(count)
n=int(input())
call=summit()
call.of digit(n)
