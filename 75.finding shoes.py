# cook your dish here

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x-y<=0:
        print(x)
    else:
        print(x-y+x)
        
        
        
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    n,m=map(int,input().split())
    if(n-m<=0):
        print(n)
    else:
        print(n-m+n)
    
    
    
    
t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    if(a<=b):
        print(a)
    else:
        print(a+(a-b))
        
        
        
/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int i=0;i<t;i++){
		    int a=sc.nextInt();
		    int b=sc.nextInt();
		    if(b<a){
		       int sum= a+(a-b);
		        System.out.println(sum);
		    }
		    else{
		        System.out.println(a);
		    }
		}
	}
}









