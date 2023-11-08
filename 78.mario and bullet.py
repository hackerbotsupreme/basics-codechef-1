for i in range(int(input())):
    x,y,z = map(int,input().split())
    bt = y//x
    ans = z-bt
    if ans < 0:
        ans = 0
    print(ans)
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
        x,y,z=map(int,input().split())
        print(z-(y//x)) if (z-(y//x))>0 else print(0)
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    if(y%x==0 && z>y/x)
	    cout<<z-(y/x)<<endl;
	    else if(z<=y/x)
	    cout<<0<<endl;
	    else
	    cout<<y/x<<endl;
	}
	return 0;
}




