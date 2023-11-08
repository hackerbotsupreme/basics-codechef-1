# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    c=x-y
    a=math.fabs(c)//2
    
    if math.fabs(c)%2==0:
        print(int(a))
    else:
        print(int(a+1))
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while (t--)
	{
	    int x,y,dist;
	    cin >> x >> y;
	    dist = abs(x-y);
	    if (dist == 1)
	    {
	        cout << 1 << endl;;
	    }
	    else if (dist%2 == 0)
	    {
	        cout << dist/2 << endl;
	    }
	    else if (dist%2 !=0)
	    {
	        cout << (dist/2) + 1 << endl;
	    }
	}
	return 0;
}










#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while (t--)
	{
	    int x,y,dist;
	    cin >> x >> y;
	    dist = abs(x-y);
	    if (dist == 1)
	    {
	        cout << 1 << endl;;
	    }
	    else if (dist%2 == 0)
	    {
	        cout << dist/2 << endl;
	    }
	    else if (dist%2 !=0)
	    {
	        cout << (dist/2) + 1 << endl;
	    }
	}
	return 0;
}






