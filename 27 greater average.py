# cook your dish here
for t in range(int(input())):
    a,b,c = map(int,input().split())
    if(((a+b)/2)>c):
        print("yes")
    else:
        print('no')
        
        
        
        
# cook your dish here
t = int(input())
while t > 0:
    a,b,c = map(int,input().split())
    if (((a + b) / 2) > c):
        print("YES")
    else:
        print("NO")
    t-=1
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	float a,b,c;
	float n;
	while(t--){
	    cin>>a>>b>>c;
	    n = (a+b)/2 ;
	    if((n) > c){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}








#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    double a,b,c;
	    cin>>a>>b>>c;
	    double z=(a+b)/2;
	    if(z>c) cout<<"YES"<<endl;
	    else cout<<"NO"<<endl;
	}
	return 0;
}

