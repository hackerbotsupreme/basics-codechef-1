for _testcase in range(int(input())):
    a,b,c = map(int, input().split())
    d,e,f, = map(int, input().split())
    if (a + b + c) == (d + e + f): print('Pass')
    else: print('Fail')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        a=list((map(int,input().split())))
        x=list((map(int,input().split())))
        if a.count(1)==x.count(1):
                print("Pass")
        else:
                print("Fail")
                
                
                
                
                
                
                
                
                
                
                
                
                
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int i,n,t;
	cin>>t;
	while(t--)
	{
	 int a[3],b[3],c=0,d=0;
	 for(i=0;i<3;i++)
	  {
	      cin>>a[i];
	  }
	  for(i=0;i<3;i++)
	  {
	      cin>>b[i];
	  }
	   for(i=0;i<3;i++)
	  {
	      if(a[i]==1)
	      {
	       c++;
	      }
	      if(b[i]==1)
	      {
	       d++;
	      }
	  }
	  if(c==d)
	  cout<<"Pass"<<endl;
	  else
	  cout<<"Fail"<<endl;
	}
	return 0;
}













#include <iostream>
using namespace std;

int main() {
    int l,p,q,r,s,t,u,a;
    cin>>l;
    while(l--)
    {   int b;
        cin>>p>>q>>r>>s>>t>>u;
        a=p+q+r;
        b=s+t+u;
        if(a==b)
        {
            cout<<"Pass"<<endl;
        }
        else
        {
            cout<<"Fail"<<endl;
        }
        
    }
	// your code goes here
	return 0;
}