# cook your dish here
import math

def find_max(a,b):
    if(a>b):
        return a
    else:
        return b
        
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a%2==0 and b%2==0 and abs(a-b)==2):
        print("YES")
    elif(a%2!=0 and b%2!=0 and abs(a-b)==2):
        print("YES")
    else:
        maxi=find_max(a,b)
        if(maxi%2==0 and abs(a-b)==1):
            print("YES")
        else:
            print("NO")
        
        
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	// your code goes here
	int T = 0;
	int a,b;
	scanf("%d\n",&T);
	for (int i = 0;i < T; i++)
	{
	    scanf("%i %i",&a,&b);
	    int diff = a-b;
	    if (diff < 0)
	    	diff *= -1;
	    if (diff > 2)
	    	printf("NO\n");
	    else if ((a % 2 == 0) && (a + 1 == b))
	    	printf("NO\n");
	    else if ((a % 2 != 0) && (a - 1 == b))
	    	printf("NO\n");
	    else
	    	printf("YES\n");
	}
	return 0;
}




















#include <stdio.h>
int main(void) {
	int a,b,n;
	scanf("%d",&n);
	while(n--)
	{
	    scanf("%d%d",&a,&b);
	    printf("%s\n",(a%2!=0&&a==b-1||a==b-2||a==b+2||a%2==0&&a==b+1)?"YES":"NO");
	}
	return 0;
}