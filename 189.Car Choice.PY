for t in range(int(input())):
    x1, x2, y1, y2 = map(float, input().split())
    if(y1 / x1 < y2 / x2):
        print("-1")
    elif(y2 / x2 < y1 / x1):
        print("1")
    else:
        print("0")
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        x1,x2,y1,y2=map(int,input().split())
        if y1/x1 > y2/x2:
                print(1)
        elif y1/x1 < y2/x2:
                print(-1)        
        else:
                print(0)
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  x1,x2,y1,y2 = map(int,input().split())
  p1 = y1/x1
  p2 = y2/x2
  if p1 < p2:
    print("-1")
  elif p1 > p2:
    print("1")
  else:
    print("0")
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--){
	   float  x1,x2,y1,y2;
	    scanf("%f%f%f%f",&x1,&x2,&y1,&y2);
	    if(y1/x1<y2/x2){
	        printf("-1\n");
	    }
	    else if(y1/x1>y2/x2){
	        printf ("1\n");
	    }
	    else{
	        printf("0\n");
	  
	}
	
	}

	return 0;
}










#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        float x1,x2,y1,y2;
        scanf("%f %f %f %f", &x1, &x2, &y1, &y2);
        if((y1/x1)>(y2/x2))
        {
            printf("1 \n");
        }
        else if((y1/x1)==(y2/x2))
        {
            printf("0 \n");
        }
        else
        printf("-1 \n");
        t--;
    }
	// your code goes here
	return 0;
}
