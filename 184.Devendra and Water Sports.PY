for _ in range(int(input())):
    z,y,a,b,c = map(int,input().split())
    if (z - y) >= (a + b + c):
        print('yes')
    else:print('no')
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
  Z,Y,A,B,C = map(int,input().split())
  r = Z - Y
  if r >=A+B+C:
    print("YES")
  else:
    print("NO")
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int z, y, a, b, c;
	    cin>>z>>y>>a>>b>>c;
	    
	    cout<< (z-y >= a+b+c ? "YES":"NO") <<endl;
	}
	return 0;
}