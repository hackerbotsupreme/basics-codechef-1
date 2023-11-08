# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    k=x%3
    if (k%3)==0:
     print(k%3)
    else:
        
     print(3-k%3)
     
     
     
import math
for _ in range(int(input(" "))):
    n=int(input())
    x=(math.ceil(n/3))
    y=(x*3)
    print((y-n))
        



#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--){
	    int x;
	    scanf("%d",&x);
	    if(x%3!=0){
	    printf("%d\n",3-(x%3));}
	    else{
	        printf("0\n");
	    }
	}
	return 0;
}


