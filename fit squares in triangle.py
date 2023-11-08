# cook your dish here
for i in range(int(input())):
        a,b=map(int,input().split())
        l=list(map(int,input().split()))
        count=0
        for i in l:
                if i>b:
                        count+=1
        print(count)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
import math
for _ in range(int(input())):
    n=int(input())
    s = math.floor(n/2)
    print(int(((s-1)*(s))/2))
    # First will find sum up to n using recursion then print sum - n for the maximum number of squares ,























#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int b, a;
	    cin>>b;
	    a = b/2 -1;
	    
	    if (a <= 0) cout<< 0 <<endl;
	    else cout<< a*(a+1)/2 <<endl;
	}
	return 0;
}



















#include <iostream>
using namespace std;

int sum(int n){
    if(n == 0 || n==1){
        return n;
    }
    return n + sum(n-1);
}

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,x;
	    cin>>n;
	    x = n/2; 
	    cout<<sum(x)-x<<endl;
	}
	return 0;
}