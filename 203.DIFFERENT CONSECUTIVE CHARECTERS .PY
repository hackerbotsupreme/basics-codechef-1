for t in range(int(input())):
    c = 0
    n = int(input())
    S = input()
    for i in range(n - 1):
        if S[i] == S[i+1]:
            c+=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    a=int(input())
    b=input()
    ans=0
    for i in range(len(b)):  
        if (i)<len(b)-1:
            if b[i]==b[i+1]:
                ans+=1 
            else:
                ans+=0
        else:
            break 
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    for i in range(n-1):
        if(s[i]==s[i+1]):
            c+=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,c=0;
        cin>>n;
        string s;
        cin>>s;
        for(int i=0;i<n;i++)
        {
            if(s[i]==s[i+1])
            {
                c++;
            }
        }
        cout<<c<<endl;
    }
	return 0;
}