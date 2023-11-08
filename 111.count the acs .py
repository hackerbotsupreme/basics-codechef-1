for _ in range(int(input())):
    n=int(input())
    r=n%100+n//100
    if r<=10:
        print(r)
    else:
        print("-1")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int p;
	    cin>>p;
	    int i = (p/100)+(p%100);
	    if(i<=10){
	        cout<<i<<endl;
	    }
	    else{
	        cout<<-1<<endl;
	    }
	}
	return 0;
}









#include <iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int p;
        cin>>p;
        if(p<=10)
        {
            cout<<p<<endl;
        }
        else if(p<100 && p>10)
        {
            cout<<-1<<endl;
        }
        else if(p>100 && (p%100)>(10-p/100))
        {
            cout<<-1<<endl;
        }
        else if(p>=100)
        {
            cout<<(p/100 + p%10)<<endl;
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
	    int p;
	    cin>>p;
	    int r,s;
	    r=p/100;
	    s=p%100;
	    if(r+s<=10)
	    {
	        cout<<r+s<<endl;
	    }
	    else
	    {
	        cout<<"-1"<<endl;
	    }
	}
	return 0;
}