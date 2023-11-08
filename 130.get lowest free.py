# cook your dish here
for i in range(int(input())):
        a,b,c=map(int,input().split())
        print((a+b+c)-min(a,b,c))
        
        
        
        
for i in range(int(input())):
    x=list(map(int,input().split()))
    print(sum(x)-min(x))
    













#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >>n;
    while (n--){
        int a,b,c;
        cin>>a>>b>>c;
        int ans = max({a+b,b+c,a+c});
        cout<<ans<<endl;
    }
}












#include <iostream>
#include<cmath>
using namespace std;

int main() {
	// your code goes here
	int t,a,b,c;
	cin>>t;
	while(t--){
	    cin>>a>>b>>c;
	    int k = min(a,min(b,c));
	    cout<<a+b+c-k<<endl;
	}
	return 0;
}