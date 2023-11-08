T=int(input())
for o in range(T):
    X1,Y1,X2,Y2=map(int,input().split())
    if X1==X2 or Y1==Y2:
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    if x==a or y==b:
        print('YES')
    else:
        print('NO')
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        a,b,x,y=map(int,input().split())
        print("YES") if a==x or b==y else print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int x1,x2,y1,y2;
	    cin>>x1>>x2>>y1>>y2;
	    if(x1==y1)
	    {
	        cout<<"YES"<<endl;
	    }
	    else if(x2==y2)
	    {
	        cout<<"YES"<<endl;
	    }
	    else
	    {
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}


















#include <bits/stdc++.h>
using namespace std;

int main()
{
  int tt;
  cin >> tt;
  while(tt--)
  {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    if(x1 == x2 || y1 == y2) cout << "YES" << "\n";
    else cout << "NO" << "\n";
  }
  return 0;
}