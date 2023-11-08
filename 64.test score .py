# cook your dish here
t=int(input())
for i in range(t):
        n,x,y=map(int,input().split())
        print("YES") if (y%x==0) else print("NO")
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    print("YES") if x%n==0 else print("NO")
    
    
    
# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    x=x%n
    if(x==0):
        print("YES")
    else:
        print("NO")
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,x;
	    cin>>n>>x;
	    if(x>=n && x%n==0)
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







#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        if(x%n==0)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
	return 0;
}





#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,x;
	    cin>>n>>x;
	    if(n-x==0 && n%x==0 || x%n==0)
	    cout<<"YES"<<endl;
	    else
	    cout<<"NO"<<endl;
	}
	return 0;
}