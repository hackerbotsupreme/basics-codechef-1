# cook your dish here
#we know y is gonna be negative , so maximumm product will be along the lines of -1, -2 etc and not -2552 (random number) 
#so for product to be maximum the x should be minimum
#minimum x is nothing but 1
#now y = sum - 1 
#and y is negative therefore y= -sum-1
T = int(input())
for i in range(T):
    s = int(input())
    print(-s-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
for tc in range(int(input())):
    s=int(input())
    #x,y=0,0
    #as for the maximum possible product if y is minimum and x=1
    #y=-s-1
    #y=-1-1=-2(minimum)
    #y*y=(-2)*(-2)=4(maximum)
    print(-s-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
using System;
public class Code
{
	public static void Main(string[] args)
	{
	    int t = Convert.ToInt32(Console.ReadLine());
	    for(int i = 1; i <= t; i++) {
	        int s = Convert.ToInt32(Console.ReadLine());
	        int r = (-s) - 1;
            Console.WriteLine(r);
	    }
	}
}





















/*

Hello coder!!!

Welcome to my solution (hope its correct XD). I just wanted to tell you that  if 
you want a bit more explanation  about this problem then you can visit my github
repository where I have posted a brief explanation of answer. 

Feel free to check it out , if you feel that my code can be optimized then
please create a pull request to update the solution. So in that way it can be 
helpful for others too.

Thanks and happy coding :)

**my github repo link**
https://github.com/soniyash9000/Code_chef_Solutions

*/


#define ll long long
#define f(end) for(int i=0;i<end;i++)
#define e '\n'
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t,n;
	cin>>t;
	while(t--)
	{
	 cin>>n;
	 cout<<0-(n+1)<<e;
	}
	return 0;
}