class ifisodd:
	def sum(self,n,m):
		s=n+m
		if s%2==0:
			print("even")
		else:
			print("odd")
n,m=map(int,input().split())
call=ifisodd()
call.sum(n,m)
