#include<stdio.h>
int main()
{
intn,num,rev=0;
printf("Enter any number to check palindrome:");
scanf("%d",&n)
num=n;
while(n!=0)
{
rev = (rev*10)+(n%10);
n/=10;
}
if(rev == num)
{
printf("%d yes.",num);
}
else
{
printf("%d no.",num);
}
return 0;
}
