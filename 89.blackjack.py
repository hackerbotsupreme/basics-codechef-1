# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if(a+b>=11):
        print(21-(a+b))
    else:
        print(-1)
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c= 21 -  (a + b) 
    if c<=10:
        print(c)
    else:
        print("-1")






# cook your dish here
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(21-(a+b) if (21-(a+b)) <= 10 else -1)
#    k = 21-(a+b)
#    if k <= 10:
#        print(k)
#    else:
#        print(-1)




#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b;
	    cin>>a>>b;
	    if(a+b<=10)
	    cout<<-1<<endl;
	    else
	    cout<<21-(a+b)<<endl;
	    
	}
	return 0;
}








/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner(System.in);
	    int t;
	    t=sc.nextInt();
	    while(t-->0){
	        int a,b;
	        a=sc.nextInt();
	        b=sc.nextInt();
	         int d=0;
	        for(int i=1;i<=10;i++){
	           d=a+b+i;
	            if(d==21) { System.out.println(i); break;}
	           }
	           if(d!=21) System.out.println(-1);   
	        
	        	    }
		// your code goes here
	}
}