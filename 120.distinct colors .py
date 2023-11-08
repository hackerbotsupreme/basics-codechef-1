# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        print(max(k))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  N = int(input())
  K = list(map(int,input().split()))
  print(max(K))
  
  
  
  
  
  
  
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	    }
	    for(int i=1;i<n;i++){
	        if(a[0]<a[i]){
	            a[0]=a[i];
	        }
	    }
	    cout<<a[0]<<endl;
	}
	return 0;
}








#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int>v(n);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        sort(v.begin(),v.end());
        cout<<v[n-1]<<"\n";
    }
	return 0;
}