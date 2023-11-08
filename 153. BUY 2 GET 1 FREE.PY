# cook your dish here
for i in range(int(input())):
        n,x=map(int,input().split())
        print((n-(n//3))*x)
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main(){

        int n;
        cin>>n;
	    for(int i=0;i<n;i++)
	    {
	        int x,y;
	        cin>>x>>y;
	      cout<<(x-x/3)*y<<endl;
	     }
	    
	
	return 0;
}






#include <iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		int x,y;
		cin>>x>>y;
		int cost=0;
		for(int i=1;i<=x;i++){
			if(i%3==0){
				cost=cost+0;
			}
			else{
				cost=cost+y;
			}
		}
		cout<<cost<<endl;
	}
 }





