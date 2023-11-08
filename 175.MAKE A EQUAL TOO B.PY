#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	{
	    int a,b;cin>>a>>b; 
	    if (a==b) 
	    cout<<"yes"<<endl;
	    else if (a<b)
	    {
	        while(a<b)
	        {
	            a=2*a;
	           
	        }if (a==b)
	        cout<<"yes"<<endl;
	        else
	        cout<<"no"<<endl;
	    }
	    else if (a>b)
	    {
	        while(b<a)
	        {
	            b=2*b;
	        }if (a==b)
	        cout<<"yes"<<endl;
	        else
	        cout<<"no"<<endl;
	    }
	    
	}
	
	    return 0;
}











#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	{
	    int a,b;cin>>a>>b; 
	    if (a==b) 
	    cout<<"yes"<<endl;
	    else if (a<b)
	    {
	        while(a<b)
	        {
	            a=2*a;
	           
	        }if (a==b)
	        cout<<"yes"<<endl;
	        else
	        cout<<"no"<<endl;
	    }
	    else if (a>b)
	    {
	        while(b<a)
	        {
	            b=2*b;
	        }if (a==b)
	        cout<<"yes"<<endl;
	        else
	        cout<<"no"<<endl;
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
	
	while(t--) {
	    int a, b, c, d;
	    cin>>a>>b;
	    
	    string s = "NO";
	    
	    if (a==b) s = "YES";
	    else if (a<b) {
	    while(a<b) {
	        a *= 2;
	        if (b == a) {
	            s = "YES";
	            break;
	        }
	    }
	    }
	    else if (b<a) {
	        while (b<a) {
	            b *= 2;
	            if (a == b) {
	                s = "YES";
	                break;
	            }
	        }
	    }
	    cout<<s<<endl;
	}
	return 0;
}