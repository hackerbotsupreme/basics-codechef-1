# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    if(x%10 == 0):
        print(0)
    elif(x%5==0):
        print(1)
    else:
        print(-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    if(x%10 == 0):
        print(0)
    elif(x%5==0):
        print(1)
    else:
        print(-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int x;
	    cin>>x;
	    
	    if (x%5 != 0) cout<<-1;
	    else {
	        if (x%10 == 0) cout<<0;
	        else {
	            for (int i=0; i<100; i++) {
	                x *= 2;
	                if (x%10 == 0) {
	                    cout<<i+1;
	                    break;
	                }
	            }
	        }
	    }
	    cout<<endl;
	}
	return 0;
}