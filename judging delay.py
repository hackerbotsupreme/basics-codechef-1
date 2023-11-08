# cook your dish here
for _ in range(int(input())):
    count=0
    for i in range(int(input())):
        a,b=map(int,input().split())
        if(abs(a-b)>5):
            count+=1
    print(count)
    
    
    
    
    
    
# cook your dish here
# cook your dish here
for _ in range(int(input())):
    count=0
    for i in range(int(input())):
        a,b=map(int,input().split())
        if(abs(a-b)>5):
            count+=1
    print(count)
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	int n,a,b,count=0;
	cin>>n;
	while(n--){
	    cin>>a>>b;
	    int diff=b-a;
	    if(diff>5)
	    count++;
	}
	cout<<count<<endl;
	    
	}
	
	return 0;
}












#include <stdio.h>

int main(void) {
    int t;
    scanf("%d \n",&t);
    while(t--)
    {
        int n;
        scanf("%d \n",&n);
        if(n>=5)
        {
            int x[n],y[n],count=0;
            for(int i=0;i<n;i++)
            {
              scanf("%d %d",&x[i],&y[i]);
            }
               for(int i=0;i<n;i++)
               {
                   if(y[i]-x[i]>5)
                   count++;
               }
            
            
            printf("%d \n",count);
        }
    }
	return 0;
}
