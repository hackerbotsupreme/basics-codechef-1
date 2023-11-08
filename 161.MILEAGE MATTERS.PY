# cook your dish here
for i in range(int(input())):
        n,x,y,a,b=map(int,input().split())
        if ((n/a)*x < (n/b)*y):
                print("PETROL")
        elif ((n/a)*x > (n/b)*y):
                print("DIESEL")
        else:
                print("ANY")
                
                
                
                
                
                
                
                
                
                
                
# cook your dish here
for _ in range(int(input())):
    n,x,y,a,b=map(int,input().split())
    p=(n/a)*x
    d=(n/b)*y
    if(p<d):
        print("PETROL")
    elif(p==d):
        print("ANY")
    else:
        print("DIESEL")
        
        
        
        
        
        
        
        
        
        
        
#include <bits/stdc++.h>
#define ll long long
#define loop(i,n) for(int i=0;i<n;i++)
#define loop1(i,n) for(int i=1;i<=n;i++)
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    float n,x,y,a,b,d,p;
	    cin>>n>>x>>y>>a>>b;
	    p=(n/a)*x;
	    d=(n/b)*y;
	    if(p<d)
	    {
	        cout<<"PETROL"<<endl;
	    }
	    if(d<p)
	    {
	        cout<<"DIESEL"<<endl;
	    }
	    if(p==d)
	    {
	        cout<<"ANY"<<endl;
	    }
	    
	    
	    
	    
	}
	return 0;
}













#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    float n,x,y,a,b;
	    cin>>n>>x>>y>>a>>b;
	    if((n/a)*x>(n/b)*y)
	    cout<<"DIESEL"<<endl;
	    else if((n/a)*x<(n/b)*y)
	    cout<<"PETROL"<<endl;
	    else
	    cout<<"ANY"<<endl;
	}
	return 0;
}






















#include<stdio.h>
int main(void)
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        float N,X,Y,A,B;
        scanf("%f",&N);
        scanf("%f",&X);
        scanf("%f",&Y);
        scanf("%f",&A);
        scanf("%f",&B);
        float H=(N*X)/A;
        float P=(N*Y)/B;
        if(H>P)
        printf("DIESEL\n");
        else if(P>H)
        printf("PETROL\n");
        else 
        printf("ANY\n");
    }
    return 0;
}






