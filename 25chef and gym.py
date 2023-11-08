# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if(x+y<=z):
        print(2)
    elif(x<=z):
        print(1)
    else:
        print(0)
        
        
        
        
        
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if (x + y) <= z:
        print('2')
    elif  x <= z:
        print('1')
    else:
        print('0')
        
        
        
        
        
# cook your dish here
t = int(input())
while t > 0:
    x,y,z = map(int,input().split())
    if x + y <= z:
        print("2")
    elif x <= z:
        print("1")
    else:
        print("0")
    t-=1
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while (t--)
	{
	    int x,y,z;
	    scanf("%d%d%d",&x,&y,&z);
	    if(x+y<=z)
	    {
	        printf("2\n");
	    }
	    else if(z>=x)
	    {
	        printf("1\n");
	    }
	    else{
	        printf("0\n");
	    }
	}
	return 0;
}
