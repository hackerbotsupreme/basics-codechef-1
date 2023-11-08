# cook your dish here
for i in range(int(input())):
        n,m=map(int,input().split())
        print("YES") if (n/m)%2==0 else print("NO")
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    k=n/m
    if k%2==0 and n%m==0:
        print("Yes")
    else:
        print("No")
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x/y
    if a%2==0:
        print("Yes")
    else:
        print("No")
    
    
/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
Scanner S=new Scanner (System.in);
int T=S.nextInt();
for(int i=0;i<T;i++) {
  int N=S.nextInt();
  int M=S.nextInt();
  if(N%M==0 && (N/M)%2==0) {
      System.out.println("YES");
  }
  else
   System.out.println("NO");
}
}
}