import java.util.*;
import java.io.*;
class Decimals
{
  public static void main(String args[])
  {
        double a, b;
        Scanner input = new Scanner(System.in);
    	a=input.nextFloat();
	b=input.nextFloat();
	double c=a*b;
	System.out.format("%.5f",c);
  }
}
