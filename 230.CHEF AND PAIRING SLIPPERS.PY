# cook your dish here
t=int(input())
for i in range(t):
    n,l,x=map(int,input().split())
    if (n-l)==l:
        print(l*x)
    elif (n-l)>l:
        print(l*x)
    else:
        print((n-l)*x)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
t=int(input())
for i in range(t):
    n,l,x=map(int,input().split())
    r=n-l
    print(min(l,r)*x)
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        n,l,x=map(int,input().split())
        if n-l>=l:
                print(l*x)
        elif n-l<l:
                print((n-l)*x)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,l,x,a;
        cin>>n>>l>>x;
        a=n-l;
        if(a>=l)
        cout<<l*x<<endl;
        else
        cout<<a*x<<endl;
        
    }
	// your code goes here
	return 0;
}




