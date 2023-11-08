# cook your dish here
for i in range(int(input())):
        s,x,y,z=map(int,input().split())
        if (x+y)+z<=s:
                print("0")
        elif (x+z)<=s or (y+z)<=s:
                print("1")
        else:
                print("2")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int s, x, y, z;
	    cin>>s>>x>>y>>z;
	    
	    if (s < x+y+z) {
	        if (s>=y+z || s>=x+z) cout<<1;
	        else cout<<2;
	    }
	    else cout<<0;
	    cout<<endl;
	}
	return 0;
}














#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while (t--){
	    int s,x,y,z;
	    cin>>s>>x>>y>>z;
	    if ((x+y+z)<=s){
	        cout<<0<<endl;
	    }else if (x+z<=s ||y+z<=s ){
	        cout<<1<<endl;
	    }else {
	        cout<<2<<endl;
	    }
	}
	return 0;
}