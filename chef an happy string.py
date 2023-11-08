# cook your dish here
for _ in range(int(input())):
    D,d,A,B,C=map(int,input().split())
    res=d*D 
    prize=0 if res<10 else(C if res>=42 else (B if res>=21 else A))
    print(prize)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        D,d,a,b,c=map(int,input().split())
        if D*d<10:
                print(0)
        elif (D*d>=10 and D*d<21):
                print(a)
        elif (D*d>=21 and D*d<42):
                print(b) 
        else:
                print(c)
                
                
                
                
                
                
                
                
                
                
                
                
# cook your dish here
for _ in range(int(input())):
    x,y,a,b,c = map(int,input().split())
    if(x*y >= 42):
        print(c)
    elif(x*y >= 21):
        print(b)
    elif(x*y >= 10):
        print(a)
    else:
        print(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
    int t;cin>>t;
    while(t--)
    {
        int D,d,a,b,c;
        cin>>D>>d>>a>>b>>c;
        int cal=D*d;
        if(cal<10)
        {
            cout<<"0"<<endl;
        }
        else if(cal>=10 && cal<21)
        {
            cout<<a<<endl;
        }
        else if(cal>=21 && cal<42)
        {
            cout<<b<<endl;
        }
        else
{
    cout<<c<<endl;
}
    }
	// your code goes here
	return 0;
}