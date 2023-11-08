# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n%7>5:
        print(int(n/7+1))
    else:
        print(int(n/7))
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int n;
	    cin>>n;
	    
	    cout<< (n/7) + (n%7==6 ? 1 : 0) <<endl;
	    // cout<< (n%7==6 ? n/7 +1 : n/7) <<endl;
	}
	return 0;
}