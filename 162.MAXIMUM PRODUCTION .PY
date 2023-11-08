

# cook your dish here
for i in range(int(input())):
        d,x,y,z=map(int,input().split())
        print(max(x*7,y*d+(z*(7-d))))
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() 
{
      int t;
	  cin>>t;
	while(t--)
	{
	    int d,x,y,z;
	    cin>>d>>x>>y>>z;
	    int a = 7*x;
	    int b = (y*d+(7-d)*z);
	   cout<<max(a,b)<<endl;
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
		int firstD,x,y,z,work1,work2;
		cin>>firstD>>x>>y>>z;
		work1=7*x;
		work2=(y*firstD)+(z*(7-firstD));
		cout<<max(work2,work1)<<endl;
	    
	    
	    
	    
	    
	}
	return 0;
}



















#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int d,x,y,z;
	    cin>>d>>x>>y>>z;
	    int a=x*7;
	    int b=z*(7-d)+(y*d);
	    if(a>=b){
	        cout<<a<<endl;
	    }
	    else{
	        cout<<b<<endl;
	    }
	}
	return 0;
}


