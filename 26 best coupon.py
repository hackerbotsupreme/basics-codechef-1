# cook your dish here
for i in range(int(input())):
    x=int(input())
    y=int(x*0.1)
    z=100
    if y>z:
        print(y)
    else:
        print(z)
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    x = int(input())
    print(max(int(0.1*x),(100)))
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t,x;
	cin>>t;
	while(t--){
	    cin>>x;
	    if(x*0.10>100){
	        cout<<x*0.10<<endl;
	    }else{
	        cout<<"100"<<endl;
	    }
	}
	return 0;
}







