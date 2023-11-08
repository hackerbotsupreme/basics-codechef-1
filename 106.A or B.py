# cook your dish here
for i in range(int(input())):
        x,y=map(int,input().split())
        a=(500-x*2)+(1000-(x+y)*4)
        b=(1000-y*4)+(500-(x+y)*2)
        print(max(a,b))
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        x,y=map(int,input().split())
        a=(500-x*2)+(1000-(x+y)*4)
        b=(1000-y*4)+(500-(x+y)*2)
        print(max(a,b))
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    int x, y;
	    cin >> x >> y;
	    //  for 1st A -> B attempt
	    int i = 500 - (x*2);
	    int j = 1000 - ((x+y)*4);
	    // for 2nd B -> A attempt
	    int p = 1000 - (y*4);
	    int q = 500 - ((x+y)*2);
	    cout << max((i+j),(p+q)) << endl;
	    
	}
	return 0;
}








#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,a,b;
	cin >> t;
	while (t--)
	{
	    cin >> a >> b;
	    int aThenB = 500 - 2*a + 1000-4*(a+b);
	    int bThenA = 1000 - 4*b + 500-2*(a+b);
	    if (aThenB > bThenA)
	    {
	        cout << 500-2*a + 1000-4*(a+b) << endl;
	    }
	    else
	    {
	        cout << 500-2*(a+b) + 1000-4*b << endl;
	    }
	}
	return 0;
}












// Asked

// Approach

#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
	while (T--){
	    int N, M;
	    cin >> N >> M;
	    int result;

	    int Y = (1000 - M*4)+  500 - (M+N)*2;
	    int X = (500 - N*2) + 1000 - (N+M)*4;
	    
	    cout << max(X, Y) << '\n';
	    
	}
	return 0;
}







