# cook your dish here
t=int(input())
while t>0:
    a,b=map(int,input().split())
    print(abs(a-b))
    t-=1
    
    
    
# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    print(abs(x-y))
    

# cook your dish here
t=int(input())
for i in range(t):
        x,y=map(int,input().split())
        print(abs(x-y))
        
        
# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    print(abs(x-y))
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    if(y>=x)
	    cout<<y-x<<endl;
	    else 
	    cout<<x-y<<endl;
	}
	return 0;
}