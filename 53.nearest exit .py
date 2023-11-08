# cook your dish here
for t in range(int(input())):
    x=int(input())
    if x<=50:
        print("LEFT")
    else:
        print("RIGHT")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
        X=int(input())
        if X>50:
                print("RIGHT")
        else:
                print("LEFT")
                
                
# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    if(a>50):
        print("RIGHT")
    else:
        print("LEFT")




#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    if(x<=50)
	    cout<<"LEFT"<<endl;
	    else
	    cout<<"RIGHT"<<endl;
	}
	return 0;
}