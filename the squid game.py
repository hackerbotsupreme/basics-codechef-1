# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        print(sum(k)-min(k))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int n, money=0;
	    cin>>n;
	    int a[n];
	    
	    for (int i=0; i<n; i++) cin>>a[i];
	    
	    sort(a, a+n);
	    for (int i=1; i<n; i++) money += a[i];
	    
	    cout<< money <<endl;
	}
	return 0;
}