# cook your dish here
t=int(input())
for i in range(0,t):
    x,y,z,a=map(int,input().split())
    sp1=x/y 
    sp2=z/a 
    if(sp1==sp2):
        print("EQUAL")
    elif(sp1>sp2):
        print("ALICE")
    else:
        print("BOB")
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        a,x,b,y=map(int,input().split())
        if ((a/x)>(b/y)):
                print("Alice")
        elif (((a/x)<(b/y))):
                print("Bob")
        else:
                print("Equal")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
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
	    float a,b,x,y;
	    cin>>a>>b>>x>>y;
	    if(a/x==b/y)
	    cout<<"EQUAL"<<endl;
	    else if(a/x>b/y)
	    cout<<"ALICE"<<endl;
	    else
	    cout<<"BOB"<<endl;
	}
	return 0;
}












#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--){
	    float a,x,b,y;
	    scanf("%f%f%f%f",&a,&x,&b,&y);
	    if((a/x)>(b/y))
	    {
	        printf("alice\n");
	}
	else if(a/x==b/y){
	    printf("equal\n");
	}
	else{
	    printf("bob\n");
	}}
	return 0;
}






#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		float a,x,b,y;
		cin>>a>>x>>b>>y;
		float alice = a/x;
		float bob = b/y;
		if(alice>bob)
		{
			cout<<" alice"<<endl;
		}
		else if(bob>alice)
		{
			cout<<" Bob"<<endl;
		}
		else
		{
			cout<<" Equal"<<endl;
		}
	}
}