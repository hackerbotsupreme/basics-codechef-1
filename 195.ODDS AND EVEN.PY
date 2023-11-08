for t in range(int(input())):
    a, b = map(int, input().split())
    if(a >= 1 and a <= 5 and b >= 1 and b <= 5):
        print("Bob" if((a + b)%2 == 0) else "Alice")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        a,b=map(int,input().split())
        print("Alice") if (a+b)%2!=0 else print("Bob")
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  a,b = map(int,input().split())
  if (a+b)%2==0:
    print("Bob")
  else:
    print("Alice")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() 
{
	ll t;
	cin>>t;
	while(t--)
	{
	    ll a,b;
	    cin>>a>>b;
	    if((a+b)%2==0)
	    cout<<"Bob"<<endl;
	    else
	    cout<<"Alice"<<endl;
	}
	return 0;
}