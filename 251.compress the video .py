# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=1
    for j in range(0,n-1):
        if a[j]!=a[j+1]:
            m+=1
    print(m)
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        l=1
        for i in range(n-1):
                if k[i]!=k[i+1]:
                        l+=1
        print(l)
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,c=0;
	    cin>>n;
	    int a[n];
	    for(int i =0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    for(int i=0;i<n;i++)
	    {
	        if(a[i]==a[i+1])
	        {
	            c++;
	        }
	    }
	    cout<<n-c<<endl;
	}
	return 0;
}












#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int i,n,t;
	cin>>t;
	while(t--)
	{
	  cin>>n;
	  int a[n],count=0;
	  for(i=0;i<n;i++)
	  {
	     cin>>a[i];
	  }
	   for(i=1;i<n;i++)
	  {
	    if(a[i-1]==a[i])
	    count++;
	  }
	  cout<<n-count<<endl;
	  
	}
	return 0;
}