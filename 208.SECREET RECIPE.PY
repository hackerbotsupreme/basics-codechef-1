for t in range (int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    if((x3 - x1) / v1  > (x2 - x3) / v2):
        print("Kefa")
    elif((x3 - x1) / v1 < (x2 - x3) / v2):
        print("Chef")
    else:
        print("Draw")
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    x1,x2,x3,v1,v2=map(int,input().split())
    c=(abs(x3-x1))/v1
    k=(abs(x3-x2))/v2
    if(c>k):
        print("Kefa")
    elif(c==k):
        print('Draw')
    else:
        print("Chef")
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for t in range (int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    if((x3 - x1) / v1  > (x2 - x3) / v2):
        print("Kefa")
    elif((x3 - x1) / v1 < (x2 - x3) / v2):
        print("Chef")
    else:
        print("Draw")
        
        
        
        
        
        
        
        
        
#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        float x1, x2, x3, v1, v2;
        scanf("%f %f %f %f %f", &x1, &x2, &x3, &v1, &v2);
        if((x3 - x1) / v1  > (x2 - x3) / v2)
            printf("Kefa\n");
        else if((x3 - x1) / v1 < (x2 - x3) / v2)
            printf("Chef\n");
        else
            printf("Draw\n");
    }
	return 0;
}
