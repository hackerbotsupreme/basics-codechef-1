# cook your dish here
t=int(input())
for i in range(t):
    s=int(input())
    if s<1500:
        g=s+s/10+s*(9/10)
    else:
        g=s+500+s*(98/100)
    print(g)    
    
    
    
    
    
# cook your dish here
# cook your dish here
for _ in range(int(input())):
    hra = 0
    da = 0
    s = int(input())
    if s < 1500 :
        hra = .1*s
        da = .90*s
    else:
        hra = 500
        da = .98*s
    print(s+hra+da)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        s=int(input())
        print(s+(0.1*s)+(0.9*s)) if s<1500 else print(s+(500)+(0.98)*s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    float salary;
	    cin>>salary;
	    
	    float hra;
	    float da;
	    if(salary>=1500)
	    {
	        hra=500;
	        da=0.98*salary;
	    }
	    else
	    {
	        hra=salary*0.1;
	        da=salary*0.9;
	    }
	    cout<<fixed<<setprecision(2)<<salary+da+hra<<endl;
	}
	return 0;
}















#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    float salary;
	    cin>>salary;
	    
	    float hra;
	    float da;
	    if(salary>=1500)
	    {
	        hra=500;
	        da=0.98*salary;
	    }
	    else
	    {
	        hra=salary*0.1;
	        da=salary*0.9;
	    }
	    cout<<fixed<<setprecision(2)<<salary+da+hra<<endl;
	}
	return 0;
}






