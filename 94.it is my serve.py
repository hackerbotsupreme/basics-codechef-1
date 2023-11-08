# cook your dish here
t = int(input())

for i in range(t):
    p,q = map(int, input().split())
    a = p+q
    if a % 4 == 1 or a % 4 ==0:
        print('Alice')
    else:
        print('Bob')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        p,q=map(int,input().split())
        if(p+q)%4==0 or (p+q)%4==1:
                print("Alice")
        else:
                print("Bob")
                
                
                
                
                
                
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int x, y, s;
	    cin>>x>>y;
	    s = (x+y)%4;
	    
	    switch (s) {
	        case 0:
	        case 1:
	            cout<<"Alice"<<endl;
	            break;
	        case 2:
	        case 3:
	            cout<<"Bob"<<endl;
	    }
	}
	return 0;
}














#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int x,y;
        cin>>x>>y;
        int e=(x+y)/2;
        if(e%2==0){
           cout<<"Alice"<<endl; 
        } 
        else{
            cout<<"Bob"<<endl;
        }
    }
	// your code goes here
	return 0;
}












#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int p,q;
	    cin>>p>>q;
	    if((p+q)%4==0 || (p+q)%4==1 ){
	        cout<<"Alice"<<endl;
	    }
	    else{
	        cout<<"Bob"<<endl;
	    }
	}
	return 0;
}