# cook your dish here

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x*100//10
    b=y*100//20 
    if(a==b):
        print("any")
    elif(a>b):
        print("first")
    else:
        print("Second")
        
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    a,b=map(int,input().split())
    if(a*10>b*5):
        print("first")
    elif(a*10<b*5):
        print("second ")
    else:
        print("any")
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    a,b=map(int,input().split())
    if(a*10>b*5):
        print("first")
    elif(a*10<b*5):
        print("second ")
    else:
        print("any")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
        a,b=map(int,input().split())
        if (a*10)>(b*5):
                print("FIRST")
        elif (a*10)<(b*5):
                print("SECOND")
        else:
                print("ANY")
                
                
                
# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    print("First") if (2*a)>b else print("second") if (2*a)<b else print("Any")
    
    
    
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int a,b,c,d;
	    scanf("%d %d",&a,&b);
	    c=10*a;
	    d=5*b;
	    if(c>d)
	    {
	        printf("FIRST\n");
	    }
	    else if(d==c)
	    {
	        printf("ANY\n");
	    }
	    else
	    {
	        printf("SECOND\n");
	    }
	}
	return 0;
}

