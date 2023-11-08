for i in range(int(input())):
    n, x =map(int, input().split())
    if x!=n:
        print(min(x, n-x))
    else:
        print(0)
        
        
        
# cook your dish here
for i in range(int(input())):
        n,x=map(int,input().split())
        print(min(x,(n-x)))
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    n,x=map(int,input().split())
    if n!=x:
        print(min(x,n-x))
    else:
        print(0)
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,x;
	    cin>>n>>x;
	    if(x==0 || n==x)
	    cout<<0<<endl;
	    else if(n-x>x)
	    cout<<x<<endl;
	    else
	    cout<<n-x<<endl;
	    
	    
	}
	return 0;
}


#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n,y;
    cin>>n>>y;
    int x = n-y;
    if(x<y) cout<<x<<endl;
    else cout<<y<<endl;
}

int main()
{
    int test;
    cin>>test;
    while(test--) solve();
    return 0;
}