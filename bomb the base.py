# cook your dish here
for t in range(int(input())):
    n,x = map(int,input().split())
    N = list(map(int,input().split()))
    m = 0
    for i in range(n):
        if(N[i]<x):
            m=i+1 
    print(m)
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    k=-1
    for i in range(n):
        if(x>a[i]):
            k=i
    print(k+1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    
    n,x=map(int,input().split())
    l1=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if l1[i]<x:
            ans= i+1  
        else:
            pass
            
    print(ans)        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    """
    houses = []
    for i in range(0,n):
        if(l[i]<x):
            for j in range(i,-1,-1):
                houses.append(j)
    print(len(set(houses)))
    """
    temp = 0
    for i in range(n-1,-1,-1):
        if(l[i]<x):
            temp = 1
            print(i+1)
            break
    if(temp == 0):
        print(0)
        
        
        
        
        
        
        
        
        
        
        
        
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int a,b,x,i,ans=-1;
	    scanf("%d %d",&a,&b);
	    for(i=0;i<a;i++)
	    {
	        scanf("%d",&x);
	        if(x<b) ans=i;
	    }
	    printf("%d\n",ans+1);
	}
	return 0;
}

        
        
        
    