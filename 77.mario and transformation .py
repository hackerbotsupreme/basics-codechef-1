# cook your dish here

t=int(input())
for i in range(t):
    x=int(input())
    if x%3==1:
        print("HUGE")
    elif x%3==2:
        print("SMALL")
    else:
        print("NORMAL")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x%3==0:
        print("normal")
    elif x%3==2:
        print("small")
    else:
        print("huge")
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    if(x%3==0)
	    cout<<"NORMAL"<<endl;
	    else if(x%3==1)
	    cout<<"HUGE"<<endl;
	    else
	    cout<<"SMALL"<<endl;
	    
	}
	return 0;
}




#include <iostream>
#include <cmath>
using namespace std;

int main() {
	// your code goes here
	int n = 0;
	cin>>n;
	while (n--){
	    // 0 - S, 1 - N, 2 - H
	    int a = 0, b = 1;
	    cin>>a;
	    for (int i = 0; i<a; i++){
	        if (b == 2){
	            b = 0;
	        } else {
	            b++;
	        }
	    }
	    if (b == 0) {
	        cout<<"SMALL\n";
	    } else if (b == 1) {
	        cout<<"NORMAL\n";
	    } else if (b == 2) {
	        cout<<"HUGE\n";
	    }
	    
	}
	return 0;
}