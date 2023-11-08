# cook your dish here
t=int(input())
for i in range(t):
    p,m,v=map(int,input().split())
    print((abs(p-m-1))*v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
T = int(input())
for _ in range(T):
    P,M,V = map(int,input().split())
    print((M-(P-1))*V)
    
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--){
	    int x,y,z;
	    scanf("%d%d%d",&x,&y,&z);
	  printf("%d\n",(y-(x-1))*z);
	        
	    
	}
	return 0;
}















T = int(input())
for _ in range(T):
    P,M,V = map(int,input().split())
    print((M-(P-1))*V)