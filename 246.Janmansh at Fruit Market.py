# cook your dish here
for i in range(int(input())):
    x,a,b,c=map(int,input().split())
    m=min(a,b,c)
    mx=max(a,b,c)
    print((x-1)*m+(a+b+c-m-mx))
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int a,b,i,n,t,c,d,e,f,g;
	cin>>t;
	while(t--)
	{
	  cin>>n>>a>>b>>c;
	  d=max(a,b);
	  e=max(d,c);
	  f=min(a,b);
	  g=min(c,f);
	  cout<<g*(n-1)+a+b+c-e-g<<endl;
	}
	return 0;
}










#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
    int k,arr[3];
    cin>>k;
    for(int l=0;l<3;l++){
        cin>>arr[l];
    }
    sort( arr, arr+3);  // sort array in incresing order
    cout<<((k-1)*arr[0]+arr[1])<<endl;
}
	return 0;
}