import java.util.*;
import java.lang.Math.*;

class subnet
	{
	public static void main(String args[])
		{
		String ip,x,mask,ipClass;
		int n,num;
		double d;
		Scanner s1=new Scanner(System.in);
		System.out.print("Enter IP Address : ");
		ip=s1.next();
		
		x=ip.substring(0,ip.indexOf("."));
		n=Integer.parseInt(x);

		System.out.println("Enter IP Address : "+n);

		if(n<128)
			{
			ipClass="A";
			mask="255.0.0.0";
			}

		else if(n>127 && n<192)
			{
			ipClass="B";
			mask="255.255.0.0";
			}

		else if(n>191 && n<224)
			{
			ipClass="C";
			mask="255.255.255.0";
			}

		else if(n>223 && n<240)
			{
			ipClass="D";
			mask="255.255.255.255";
			}

		else 
			{
			ipClass=null;
			mask=null;
			}

		System.out.println("IP Class : "+ipClass);
		System.out.println("Mask : "+mask);

		System.out.println("Enter number of subnets : ");
		num=s1.nextInt();
		d=Math.floor(Math.log(num)/Math.log(2));
		System.out.println("Masking Bits : "+d);
		int i=0;
		int t=7;
		double sum=0;
		while(i<d && d<=8)
			{
			sum=sum+Math.pow(2,t);
			t=t-1;
			i=i+1;
			}

		if(ipClass=="A") System.out.println("New Masking : 255."+Math.round(sum)+".0");
		else if(ipClass=="B") System.out.println("New Masking : 255.255."+Math.round(sum)+".0");
		else if(ipClass=="C") System.out.println("New Masking : 255.255.255."+Math.round(sum));

		}

	}

