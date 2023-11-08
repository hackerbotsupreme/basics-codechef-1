# cook your dish here
t = int(input(""))
for _ in range(t):
    n = int(input(""))
    s = input("") # initial state
    r = input("") # final state
    bulb = True
    for i in range(0, n):
        if s[i] != r[i]:
           bulb = not bulb 
    if bulb:
        print(1)
    else:
        print(0)
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    c = 0
    for i in range(n):
        if(s[i] != r[i]):
            c+=1 
    if(c%2==0):
        print(1)
    else:
        print(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <stdio.h>
#include <string.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int a,i,c=0;
	    scanf("%d",&a);
	    char s[a+1],r[a+1];
	    for(i=0;i<=a;i++)
	    {
	        scanf("%c",&s[i]);
	    }
	    for(i=0;i<=a;i++)
	    {
	        scanf("%c",&r[i]);
	        if(s[i]!=r[i])
	            c+=1;
	    }
	    if(c%2==0)
	        printf("1\n");
        else
            printf("0\n");
	}
	return 0;
}
