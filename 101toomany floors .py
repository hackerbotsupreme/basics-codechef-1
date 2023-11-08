# cook your dish here
import math
for t in range(int(input())):
    x,y=map(int,input().split())
    f1=math.ceil(x/10)
    f2=math.ceil(y/10)
    print(abs(f1-f2))
    
    
    
    
    
    
    
    
    
# cook your dish here
import math as m
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    f1=m.ceil(a/10)
    f2=m.ceil(b/10)
    print(abs(f1-f2))
    
    
    
    
# cook your dish here
import math
for i in range(int(input())):
        x,y=map(int,input().split())
        print(abs(math.ceil(y/10)-math.ceil(x/10)))
        
        
        
        
        
        
        
        
        
        
#include <stdio.h>

int main(void) {
	// your code goes here
	int test,i,j,x,y,fe,ma;
	scanf("%d",&test);
	for(j=1;j<=test;j++)
	{
	    scanf("%d%d",&x,&y);
	    if(x>y)
	    {
	        i=1;
	        while(i<=10)
	        {
	           if(x>=(10*(i-1)+1) && x<=(10*i)) 
	           {
	               ma=i;
	               i++;
	           }
	           	 
	           else
	             i++;
	        }
	        i=1;
	        while(i<=10)
	        {
              if(y>=(10*(i-1)+1) && y<=(10*i))
	           {
	               fe=i;
	               i++;
	           }
	           else
	             i++;
	        }
	        printf("%d\n",(ma-fe));
	    }
	    else if(y>x)
	    {
	        i=1;
	        while(i<=10)
	        {
	           if(x>=(10*(i-1)+1) && x<=(10*i)) 
	           {
	               ma=i;
	               i++;
	           }
	           else
	             i++;
	        }
	        i=1;
	        while(i<=10)
	        {
                if(y>=(10*(i-1)+1) && y<=(10*i))
	           {
	               fe=i;
	               i++;
	           }
	           else
	             i++;
	        }
	        printf("%d\n",(fe-ma));
	    }
	    else
	      printf("%d\n",0);
	}
	return 0;
}

# cook your dish here
import math
for i in range(int(input())):
        x,y=map(int,input().split())
        print(abs(math.ceil(y/10)-math.ceil(x/10)))