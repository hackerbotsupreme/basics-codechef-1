for _ in range(int(input())):
    n,x,p = map(int,input().split())
    if ((x*3) - (n - x)) >= p:
        print('pass')
    else:
        print('fail')
    













for _ in range(int(input())):
    n,x,p=[int(n)for n in input().split()]
    n_rem=(n-x)*(-1)
    x=x*3
    res=x+n_rem
    if res>=p:
        print("pass")
    else:
        print("fail")
        
        
        
        
        
        
        
        
        
        
        
#include <stdio.h>

int main(void) {
int t;
scanf("%d",&t);
while(t--) 
{
    int n,x,p;
    scanf("%d%d%d",&n,&x,&p);
    if((x*3+(n-x)*-1)>=p)
    {
        printf("pass\n");
    }
    else{
        printf("fail\n");
    }
}
	return 0;
}






#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n,x,p;
		cin>>n>>x>>p;
		if(4*x-n>=p)
		{
			cout<<" PASS"<<endl;
		}
		else
		{
			cout<<" FAIL"<<endl;
		}
	}
}