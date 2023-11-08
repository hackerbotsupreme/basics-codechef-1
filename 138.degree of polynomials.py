t=int(input())
for i in range(t):
    # TODO: write code...
    z1=0;
    number=int(input())
    x= list(map(int,input().split()))
    for i in range(number):
        # TODO: write code...
        if x[-1-i]==0:
            z1=z1+1;
        else:
            break 
    print(len(x)-z1-1)    
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	{
	    int n;cin>>n;int a[n]; int l=0;
	    for (int i=1;i<=n;i++)
	    {
	        cin>>a[i];
	    }
	    for(int i=1;i<=n;i++)
	    {
	        if (a[i]!=0)
	        l=i;
	    }cout<<l-1<<endl;
	}
	return 0;
}









#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    int a[n];
	    int b=INT_MIN;
	    for(int i=0 ;i<n;i++)
	    cin >> a[i];
	    int index=0;
	    for(int i=0 ;i<n;i++)
	    {
	        if( a[i] !=0 )
	        {
	            index=i;
	        }
	    }
	    cout << index << endl;
	}
	return 0;
}









#include <bits/stdc++.h>
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
	     for(int i=0;i<n;i++)
	     {
	         cin>>a[i];
	     }
	     for(int i=n-1;i>=0;i--)
	     {
	         if(a[i]==0)
	        c++;
	         else
	          break;
	     }
	     cout<<n-1-c<<endl;
	}
	
	return 0;
}