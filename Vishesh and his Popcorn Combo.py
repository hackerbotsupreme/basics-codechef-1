# cook your dish here
for t in range(int(input())):
    a1,a2 = map(int,input().split())
    b1,b2 = map(int,input().split())
    c1,c2 = map(int,input().split())
    print(max((a1+a2),(b1+b2),(c1+c2)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        long long  a1,a2;
        cin>>a1>>a2;
        long long b1,b2;
        cin>>b1>>b2;
        long long c1,c2;
        cin>>c1>>c2;
        int a=a1+a2;
        int b=b1+b2;
        int c=c1+c2;
       // int s= max(a,(b,c));
       // long s=max(((a1+a2),(b1+b2)),(c1+c2));
       // cout<<s<<endl;
       int s=max(a,b);
       int d=max(s,c);
       cout<<d<<endl;
    }
	// your code goes here
	return 0;
}




















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int a1,a2;
	    int b1,b2;
	    int c1,c2;
	    
	    cin >> a1 >> a2 >> b1 >> b2 >> c1 >> c2;
	    int x1 = a1 + a2;
	    int x2 = b1 + b2;
	    int x3 = c1 + c2;
	    
	    int maxi = max( max(x1,x2) , max(x2,x3) );
	    int maxi1 = max( maxi , max(x3,x1) );
	    cout << maxi1 << endl;
	    
	    
	}
	return 0;
}