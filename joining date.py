# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    print(math.ceil(a/5)-math.ceil(b/5))
    
    
    
    
# cook your dish here
import math
for t in range(int(input())):
    n,k = map(int,input().split())
    N = math.ceil(n/5)
    m = math.ceil(k/5)
    print(N-m)
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
import math
for t in range(int(input())):
    n,k = map(int,input().split())
    N = math.ceil(n/5)
    m = math.ceil(k/5)
    print(N-m)
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t, n, k;
	cin>>t;
	while(t--)
	{
	    cin>>n>>k;
	    if(n%5==0 && k%5==0)
	        cout<<n/5-k/5<<endl;
	    else if(n%5==0 && k%5!=0)
	        cout<<n/5-k/5-1<<endl;
	    else if(n%5!=0 && k%5==0)
	        cout<<n/5-k/5+1<<endl;
	    else
	        cout<<n/5-k/5<<endl;
	}
	return 0;
}















#include <iostream>
using namespace std;

int main() {
	int t, n, k;
	cin>>t;
	while(t--)
	{
	    cin>>n>>k;
	    if(n%5==0 && k%5==0)
	        cout<<n/5-k/5<<endl;
	    else if(n%5==0 && k%5!=0)
	        cout<<n/5-k/5-1<<endl;
	    else if(n%5!=0 && k%5==0)
	        cout<<n/5-k/5+1<<endl;
	    else
	        cout<<n/5-k/5<<endl;
	}
	return 0;
}