# cook your dish here
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    print((z*x)//y) if x%y==0 else print(((x//y)+1)*z)
    
    
    
    
# cook your dish here
import math
t=int(input())
for i in range(t):
        x,y,z=map(int,input().split())
        if y>=x:
                print(z)
        elif y<x:
                print(math.ceil(x/y)*z)
              
                
        
        
# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(x==y):
        print(z)
    elif(x<y):
        print(z)
    else:
        print(math.ceil(x/y)*z)
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    if(x%y==0)
	    cout<<(x/y)*z<<endl;
	    else
	    cout<<((x/y)+1)*z<<endl;
	    
	}
	return 0;
}


#include <iostream>
using namespace std;

int main(void) {
	int t;
	cin >> t;
	while(t--)
	{
	    int x,y,z,ans;
	    cin >> x >> y >> z;
	    if(x%y==0)
	    ans=(z*x)/y;
	    else
	    ans=((x/y)+1)*z;
	    cout << ans << endl;
	}
	return 0;
}




