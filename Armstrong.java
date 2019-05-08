import java.io.*;
import java.util.*;
public class Armstrong
{
public staticvoid main(String[]args)
{
int number=371,OriginalNumber,remainder,result=0;
OriginalNumber = number;
while (OriginalNumber!=0)
{
remainder=OrginalNumber%10;
result +=Math.pow(remainder,3);
OriginalNumber=number/=10;
}
if(result ==number)
System.out.println(number +"is an Armstrong number.");
else 
S ystem.out.println(number + "is not an Armstrongnumber.");
}
}
