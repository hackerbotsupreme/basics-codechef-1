# cook your dish here
for i in range(int(input())):
        n=int(input())
        s=input()
        if "0" in s or "5" in s:
                print("YES")
        else:
                print("NO")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    num = str(input())
    count = 0
    for i in num:
        if i=='0' or i=='5':
            count += 1
        else:
            continue
    if count>=1:
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int a,b,i,n,t;
	cin>>t;
	while(t--)
	{
	    int flag=0;
	  cin>>n;
	  string s;
	  cin>>s;
	  for(i=0;i<n;i++)
	  {
	      if(s[i]=='0' || s[i]=='5')
	      {
	          flag=1;
	          break;
	      }
	  }
	  if(flag)
	  {
	      cout<<"Yes"<<endl;
	  }
	  else
	  {
	      cout<<"No"<<endl;
	  }
	}
	return 0;
}















