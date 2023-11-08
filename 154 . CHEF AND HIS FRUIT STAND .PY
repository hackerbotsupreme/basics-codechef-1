# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if(x/2<=y):
        print(int(x/2))
    else:
        print(y)
       
       
       
       
       
       
       
       
       
       
       
# cook your dish here
for i in range(int(input())):
        x,y=map(int,input().split())
        print(min(x//2,y))
        
        
        
        
        
        
        
        
        
        
#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--) {
	    int X, Y;
	    cin >> X >> Y; int chaats=0;
	    while((X >=0 && X<=100) &&(Y >=0 && Y<=100)) {
	        X=X-2; Y--;
	        chaats++;
	    }
	    chaats--;
	    cout << chaats << endl;
	}
	return 0;
}














#include <stdio.h>

int main() {
	int n,s,r;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%d%d",&s,&r);
	   // int k;
	    if(2*r>=s)
	    {
	       printf("%d\n",s/2);
	    }
	    else
	    {
	    printf("%d\n",r);
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
	while(t--)
	{
	    int b,a;
	    cin>>b>>a;
	    int ans = b/2;
	    if(ans>a)
	    cout<<a<<endl;
	    else
	    cout<<ans<<endl;
	}
	return 0;
}