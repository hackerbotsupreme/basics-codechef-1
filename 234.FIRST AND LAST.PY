# cook your dish here
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    m=0
    for i in range(N):
        m=m if m>A[i]+A[i-1] else A[i]+A[i-1]
    print(m)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    x=int(input())
    ar=list(map(int,input().split()))[:x]
    s1=0
    s=0
    for i in range(len(ar)):
        s1=ar[i]+ar[i-1]
        if(s1>s):
            s=s1
    print(s)
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=a[0]+a[-1]
    for i in range(n-1):
        s=max(s,a[i]+a[i+1])
    print(s)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=a[0]+a[-1]
    for i in range(n-1):
        s=max(s,a[i]+a[i+1])
    print(s)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=a[0]+a[-1]
    for i in range(n-1):
        s=max(s,a[i]+a[i+1])
    print(s)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int a[n];
	    
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }
        
        int sum=a[0]+a[n-1];
        
	     for(int i=0;i<n-1;i++)
	    {
	        int temp=a[i]+a[i+1];
	        
	        sum=max(sum,temp);
	    }
	    
	    std::cout << sum << std::endl;
	}
	return 0;
}