# cook your dish here
for i in range(int(input())):
    n,k,m=map(int,input().split())
    if(n%(k*m)==0):
        print(n//(k*m))
    else:
        n=n//(k*m)
        print(n+1)
        
        
        
        


#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n,k,m;
	    cin>>n>>k>>m;
	    if(n%(k*m)==0){
	        cout<<n/(k*m)<<endl;
	    }
	    else{
	        cout<<(n/(k*m))+1<<endl;
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
	    int n,k,m,s;
	    cin>>n>>k>>m; // n candies, a bag has k pockets , each pockets can hold m candies
	    s=k*m;
	    if(n%s==0)
	    {
	        cout<<n/s<<endl;
	    }
	    else
	    {
	        cout<<(n/s)+1<<endl;
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
	while(t--)
	{
	    int a,b,c,d;
	    cin >> a>> b>> c;
	    d=b*c;
	    if(a%d ==0)
	    cout << a/d << endl;
	    else
	    cout << a/d + 1 << endl;
	}
	return 0;
}