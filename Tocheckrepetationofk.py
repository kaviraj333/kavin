n,k=map(int,input().split())
sum1=0
x=[int(i) for i in input().split()]
for i in range(0,n):
    if(k==x[i]):
        sum1=sum1+1
        print(sum1)
