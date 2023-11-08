#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	
	{
	  int n;cin>>n; int count=0;
	  while(n>0)
	  {
	    n=n/5;
	    count+=n;
	  }cout<<count<<endl;
	}
	return 0;
}
















# cook your dish here
for i in range(int(input())):
        x,y,a,b,d=map(int,input().split())
        print("YES") if (min(x/a,y/b)>=d) else print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t--){
        int x,y,xr,yr,d;
        scanf("%d%d%d%d%d",&x,&y,&xr,&yr,&d);
        if(x>=xr*d && y>=d*yr){
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
        
    }
	
	return 0;
}











#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t--){
        int x,y,xr,yr,d;
        scanf("%d%d%d%d%d",&x,&y,&xr,&yr,&d);
        if(x>=xr*d && y>=d*yr){
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
        
    }
	
	return 0;
}

        
