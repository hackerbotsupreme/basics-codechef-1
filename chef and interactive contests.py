t,n=map(int,input().split())
for i in range(t):
    x=int(input())
    if x>=n:
        print("Good boi")
    else:
        print("Bad boi")
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
a,b=map(int,input().split())
for _ in range(a):
    n=int(input())
    if(n<b):
        print("Bad boi")
    else:
        print("Good boi")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
n,r=map(int,input().split())
for i in range(n):
        R=int(input())
        print("Good boi") if R>=r else print("Bad boi")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int a,b,i,n,t;
	cin>>t>>n;
	while(t--)
	{
	  cin>>a;
	  if(a<n)
	  cout<<"Bad boi"<<endl;
	  else
	  cout<<"Good boi"<<endl;
	}
	return 0;
}