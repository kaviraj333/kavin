import java.util.Scanner;
class J88
 {
	public static void main(String[] args) 
	{
		int Num1, Num2, GCD = 0, LCM = 0;
        Scanner	sj = new Scanner(System.in);
	    int a = Num1 = sj.nextInt();	
        int b = Num2 = sj.nextInt();
		while(Num2 != 0)
	    {
			if(Num1 > Num2)
			{
				Num1 = Num1 - Num2;
			}
			else
			{
				Num2 = Num2 - Num1;
			}
	    }
		GCD = Num1;
		LCM = (a * b) / GCD;
		System.out.println(LCM);
	}
}
