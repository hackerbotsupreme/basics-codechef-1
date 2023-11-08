# cook your dish here
for t in range(int(input())):
    x,y,a,b,k=map(int,input().split())
    a=a*k
    b=b*k
    x+=a
    y+=b
    if x==y:
        print("SAME PRICE")
    else:
        if x<y:
            print("PETROL")
        else :
            print("DIESEL")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# cook your dish here
# cook your dish here
for t in range(int(input())):
    x,y,a,b,k=map(int,input().split())
    a=a*k
    b=b*k
    x+=a
    y+=b
    if x==y:
        print("SAME PRICE")
    else:
        if x<y:
            print("PETROL")
        else :
            print("DIESEL")
            
            
            
            
            
            
            
            
            
            
#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int x,y,a,b,k;
        cin>>x>>y>>a>>b>>k;
        int p=x+a*k;
        int d=y+b*k;
        if(p > d)
        cout<<"DIESEL"<<endl;
        else if(p < d)
        cout<<"PETROL"<<endl;
        else if(p == d)
        cout<<"SAME PRICE"<<endl;
    }
	// your code goes here
	return 0;
}        
