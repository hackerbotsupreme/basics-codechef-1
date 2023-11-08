goals = int(input())
for distractions in range(goals):
    wife, life, aim = map(int, input().split())
    List = list(map(int, input().split()))
    knife = List.count(life) / wife
    death = List.count(aim) / wife
    print(knife * death)
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for I in range(int(input())):
    n,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    i=l.count(a)
    j=l.count(b)
    k=(i*j)/(n*n)
    print('%.10f'%k)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for t in range(int(input())):
    n,a,b = map(int,input().split())
    N = list(map(int,input().split()))
    print(((N.count(a))*(N.count(b))/(n*n)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int a,b,c,x;
	    float b1=0,c1=0;
	    scanf("%d %d %d",&a,&b,&c);
	    for(int i=0;i<a;i++)
	    {
	        scanf("%d",&x);
	        if(x==b)
	            b1+=1;
            if(x==c)
                c1+=1;
	    }
	    printf("%f\n",(b1/a)*(c1/a));
	}
	return 0;
}