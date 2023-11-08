for _testcase in range(int(input())):
    a,b,c,d,e,f = map(int, input().split())
    if b >= a and d >= c and f <= e: print('YES')
    else: print('NO')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
  x1,x2,y1,y2,z1,z2 = map(int,input().split())
  if x1<=x2 and y1<=y2 and z1>=z2:
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
	    int x1, x2, y1, y2, z1, z2;
	    cin>>x1>>x2>>y1>>y2>>z1>>z2;
	    
	    if (x1<=x2 && y1<=y2 && z1>=z2) cout<<"YES";
	    else cout<<"NO";
	    cout<<endl;
	}
	return 0;
}












#include <iostream>
using namespace std;

int main() 
{int t,x1,x2,y1,y2,z1,z2;
    cin>>t;
    while(t--)
    {
        cin>>x1>>x2>>y1>>y2>>z1>>z2;
        if((x2>=x1)&&(y2>=y1)&&(z1>=z2))
        {
            cout<<"yes"<<endl;
        }
        else
            cout<<"no"<<endl;
    }
}