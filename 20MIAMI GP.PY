# cook your dish here
for t in range(int(input())):
    x,y = map(int,input().split())
    if(y*100 <= x*107 ):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x*107/100
    if y<=a:
        print('YES')
    else:
        print('NO')
        
        
        
        
# cook your dish here
t = int(input())
for i in range(t):
    x,y=map(float,input().split())
    if y<=1.07*x :
        print("YES")
    else:
        print("NO")
        
        
        
# cook your dish her
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<=x*107/100:
        print("yes")
        
    else:
        print("no")
        
        
        
#include <stdio.h>
#C++
int main(void) {
	int t;
	scanf("%d",&t);
	while(t!=0)
	{
	    int x,y;
	    scanf("%d%d",&x,&y);
	    if(y<=1.07*x)
	    {
	        printf("yes\n");
	        
	    }
	    else{
	        printf("no\n");
	        
	    }
	    t--;
	}
	return 0;
}

