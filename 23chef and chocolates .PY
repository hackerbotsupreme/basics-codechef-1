for i in range(int(input())):
    c,x,y=map(int,input().split())
    k=c-x
    print(k*y)
    
    
    
    
    
    
    
t = int(input())

for tc in range(t):
    c,x,y = input().split()
    c,x,y = int(c),int(x),int(y)
    res = (c-x) * y
    print(res)
    
    
    
# cook your dish here
for t in range(int(input())):
    c,x,y = map(int,input().split())
    print((c-x)*y)
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    c,x,y = map(int,input().split())
    a = c - x
    print(a*y)
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,c,x,y;
	cin>>t;
	while(t--){
	    cin>>c>>x>>y;
	    cout<<(c-x)*y<<endl;
	}
	return 0;
}
