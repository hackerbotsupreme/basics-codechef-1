# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    print((y-x)//8) if (y-x)%8==0 else print((y-x)//8+1)
    
    
    
# cook your dish here
import math
for t in range(int(input())):
    a,b=map(int,input().split())
    c=b-a
    print(math.ceil(c/8))
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    if(x>=y){
	        cout<<"0"<<endl;
	    }
	    else if((y-x)%8==0){
	        cout<<((y-x)/8)<<endl;
	    }
	    else{
	        cout<<((y-x)/8)+1<<endl;
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
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    if((y-x)%8!=0)
	    cout<<1+(y-x)/8<<endl;
	    else if((y-x)%8==0)
	    cout<<(y-x)/8<<endl;
	    else if((y-x)<=8)
	    cout<<1<<endl;
	    else
	    cout<<0<<endl;
	    
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
	    int x,y,count=0;
	    cin>>x>>y;
	    if(x>=y)
	    {
	        cout<<"0"<<endl;
	    }
	    else if((y-x)%8==0)
	    {
	        cout<<(y-x)/8<<endl;
	    }
	    else
	    {
	        cout<<((y-x)/8)+1<<endl;
	    }
	}
	return 0;
}




