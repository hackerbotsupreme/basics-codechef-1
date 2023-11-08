# cook your dish here
t = int(input())

for i in range(t):
    x,y,z=map(int,input().split())
    if y<=z:
        print(x)
    else:
        a=y//z
        if y%z==0:
            print(x*a)
        else:
            print(x*(a+1))
            
            
            
            
            
            
#include <stdio.h>

int main(void) {
	// your code goes here
	int t,x,y,z;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d %d %d",&x,&y,&z);
	    if(y%z==0)
	    printf("%d\n",(y/z)*x);
	    else
	    printf("%d\n",((y/z)+1)*x);
	}
	return 0;
}






using System;

public class Test
{
	public static void Main()
	{
		// your code goes here
		int T = int.Parse(Console.ReadLine());
		while(T>0)
		{
		    string[] s = Console.ReadLine().Split(' ');
		    int X = int.Parse(s[0]);
		    int Y = int.Parse(s[1]);
		    int Z = int.Parse(s[2]);
		    int count = 1;
		    while(Y>Z)
		    {
		        count++;
		        Y -= Z;
		    }
		    Console.WriteLine(X*count);
		    T--;
		}
	}
}