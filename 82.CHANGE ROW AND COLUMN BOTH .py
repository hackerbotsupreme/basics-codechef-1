# cook your dish here
for i in range(int(input())):
        sx,sy,ex,ey=map(int,input().split())
        if (sx!=ex) and (sy!=ey):
                print(1)
        else:
                print(2)
                
                
                
                
                
# cook your dish here
for i in range (int(input())):
    a,b,c,d=map(int,input().split())
    if(a==c or b==d):
        print("2")
    else:
        print("1")
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
    int t;
    cin>>t;
    while(t--) {
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        if(a!=c && b!=d) cout<<"1"<<endl;
        else cout<<"2"<<endl;
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
	    int sx,sy,ex,ey;
	    cin>>sx>>sy>>ex>>ey;
	    if(sx==ex || sy==ey)
	    {
	        cout<<"2"<<endl;
	    }
	    else
	    {
	        cout<<"1"<<endl;
	    }
	}
	return 0;
}