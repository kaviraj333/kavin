n=input()
n=int(n)
x=1
y=1
if(n==1):
    print(a,end='')
count=0
if(n>1):
    while(count<n):
        if(count==n-1):
            print(a,end='')
        else:
            print(a,end=' ')
        nth=x+y
        x=y
        y=nth
        count=count+1
