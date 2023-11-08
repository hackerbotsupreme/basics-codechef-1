# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>=y:
        print("yes")
    elif x+z>=y:
        print("yes")
    elif x+2*z>=y:
        print("yes")
    else:
        print("no")
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        x,y,z=map(int,input().split())
        print("YES") if (z*2+x>=y) else print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    (x,y,z) = map(int,input().split())
    need_pt=y-x
    match_pt=2*z
    if need_pt<=match_pt:
        print("yes")
    else:
        print("no")
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,x,y,z;
	cin>>t;
	while(t--){
	    cin>>x>>y>>z;
	    int k = (((2*z)+x)-y);
	    if(k<0){
	        cout<<"NO"<<endl;
	    } else{
	        cout<<"YES"<<endl;
	    }
	}
	return 0;
}









#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--){
	    int x,y,z;
	    scanf("%d%d%d",&x,&y,&z);
	    if(x+(z*2)>=y || x+(z*1)>=y){
	        printf("yes\n");
	    }
	    else{
	        printf("no\n");
	    }
	    
	}
	return 0;
}
