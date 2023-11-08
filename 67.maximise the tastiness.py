# cook your dish here
t=int(input())
for t in range(t):
    a,b,c,d=map(int,input().split())
    print(max((a+c),(a+d),(b+c),(b+d)))
    
    
    
# cook your dish here
t = int(input(""))
for _ in range(t):
    a, b, c, d = map(int, input("").split(' ',4))
    sm = max(a + c, b + c, a + d, b + d)
    print(sm)
    
    
    
    
# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    e=max(a,b)
    f=max(c,d)
    print(e+f)
    
    
    
# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(max(a,b)+max(c,d))
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;
	    cout<<max(a,b)+max(c,d)<<endl;
	}
	return 0;
}