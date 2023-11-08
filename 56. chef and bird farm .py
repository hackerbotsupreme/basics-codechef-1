
   
   
   
   
   
   
   
# cook your dish here
for t in range(int(input())):
    x,y,z=map(int,input().split())
    if z%x==0 and z%y!=0:
        print("CHICKEN")
    elif z%y==0 and z%x!=0:
        print("DUCK")
    elif z%x==0 and z%y==0:
        print("ANY")
    else:
        print("NONE",end=" ")
       
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
        x,y,z=map(int,input().split())
        if z%x==0 and z%y==0:
                print("ANY")
        elif z%x==0:
                print("CHICKEN")
        elif z%y==0:
                print("DUCK")
        
        else:
                print("NONE")
                


#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    if(z%x!=0 && z%y!=0)
	    cout<<"NONE"<<endl;
	    else if(z%x==0 && z%y==0)
	    cout<<"ANY"<<endl;
	    else if(z%x==0)
	    cout<<"CHICKEN"<<endl;
	    else if(z%y==0)
	    cout<<"DUCK"<<endl;
	    
	}
	return 0;
}



