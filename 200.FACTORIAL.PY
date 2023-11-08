# cook your dish here
def trail(n):
    count=0
    while(n>0):
        count+=n//5
        n//=5 
    print(count)
t=int(input())
while(t):
    n=int(input())
    trail(n)
    t-=1 
    
    
    
    
    
    
    
    
    
    
    
for t in range(int(input())): 
    count = 0
    n = int(input())
    while(n!=0):
        count += n//5
        n//= 5
    print(int(count))
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t , n ;
	cin>>t;
	while(t--) {
	    cin>>n;
	    int sum=0;
	    while(n>0) {
	        sum += n/5;
	        n /= 5;
	    }
	    cout<<sum<<endl;
	}
	return 0;
}












#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	
	{
	  int n;cin>>n; int count=0;
	  while(n>0)
	  {
	    n=n/5;
	    count+=n;
	  }cout<<count<<endl;
	}
	return 0;
}