# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(input().split())
    count = 0
    for i in range(n):
        a[i] = int(a[i]) + k 
        if (a[i] % 7 == 0):
            count += 1
    print(count)
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>> t ;
	while(t--)
	{
	    int x,j,y,sum,ome=0;
	    cin >> x>>y;
	    int ara[x] ;
	    for (j=0;j<x;j++)
	    {
	        cin >> ara[j];
	        sum = ara[j] + y ;
	        if (sum%7==0)
	        {
	            ome++;
	        }
	    }
	    cout <<""<<ome<<endl;
	}
	return 0;
}








#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	 int n,k;
	 cin>>n>>k;
	 int a[n];
	 for(int i=0;i<n;i++){
	     cin>>a[i];
	 }
	 int count =0;
	 for(int i=0;i<n;i++){
	     int j=(a[i]+k);
	     if(j%7==0){
	         count++;
	     }
	 }
	 cout<<count<<endl;
	    
	}
	return 0;
}