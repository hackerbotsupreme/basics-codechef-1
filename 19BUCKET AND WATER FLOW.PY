# cook your dish here
for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w+y*z>x:
        print("Overflow")
    elif w+y*z<x:
        print("unfilled")
    else:
        print("Filled")
        
        
        
        
        
        
for _ in range(int(input())):
    w,x,y,z = list(map(int,input().split()))
    if (y*z) > (x - w):
        print('overFlow')
    elif (y*z) == (x - w):
        print('filled')
    else:
        print('Unfilled')
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    if(x==w+(y*z)):
        print("filled")
    elif(x>w+(y*z)):
        print("unfilled")
    else:
        print("overflow")
        
        
        
        
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    w,x,y,z = map(int,input().split())
    if(x>(z*y + w)):
        print("unfilled")
    elif(x==(z*y + w)):
        print("filled")
    else:
        print("overflow")
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;         //w->qty ini, x->max cap., y-> rate l/h, 
	                //z-> tap open time
	while(t--)      
	{
	    int w,x,y,z;
	    cin>>w>>x>>y>>z;
	    if((x-w)==(y*z))
	        cout<<"filled"<<endl;
	    else if((x-w)>(y*z))
	        cout<<"Unfilled"<<endl;
	    else if(w>x)
	        cout<<"overflow"<<endl;
	    else
	        cout<<"overflow"<<endl;
	        
	    
	}
	return 0;
}




