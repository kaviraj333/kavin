import java.io.*;
public class Numeric
{
String string = "12345.15";
boolean numeric=true;
try 
{
Double num = Double.parseDouble(string);
}
catch(NumberFormatException e )
{
numeric=false;
}
if(numeric)
System.out.println(string +"is a number");
else
System.out.println(string +"is not a number");
}
}
