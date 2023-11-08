# cook your dish here
for I in range(int(input())):
    a,b,c,d=map(int,input().split())
    if((a*a)/(c*c*c)==(b*b)/(d*d*d)):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    t1,t2,r1,r2=map(int,input().split())
    a=(t1*t1)/(r1*r1*r1)
    b=(t2*t2)/(r2*r2*r2)
    if(a==b):
        print('Yes')
    else:
        print('No')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    t1,t2,r1,r2=map(int,input().split())
    a=t1**2/r1**3
    b=t2**2/r2**3
    if a==b:
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include<cmath>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int t1,t2,r1,r2;
	    cin>>t1>>t2>>r1>>r2;
	    float a=pow(t1,2)/pow(r1,3);
	    float b=pow(t2,2)/pow(r2,3);
	    if(a==b)
	        cout<<"yes"<<endl;
	    else
	        cout<<"no"<<endl;
	}
	return 0;
}s