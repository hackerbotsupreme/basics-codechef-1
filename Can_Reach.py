for _ in range(int(input())):
    x,y,k=map(int,input().split())
    print("NO") if(abs(x)%k!=0 or abs(y)%k!=0) else print("YES")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    x,y,k=map(int,input().split())
    if(x%k==0 and y%k==0):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
// #include <stdlib.h>
#include <math.h>
using namespace std;


int main()
{
    int testcase;
    cin >> testcase;
    for (int testcase_variable = 0; testcase_variable < testcase; testcase_variable++)
    {
        int x,y,k;
        cin>>x>>y>>k;
        if (abs(x)%k==0 && abs(y)%k==0)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
}

