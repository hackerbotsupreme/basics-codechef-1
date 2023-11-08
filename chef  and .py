# cook your dish here
for i in range(0, int(input())):
    a,b,c=map(int,input().split())
    maxi=max(a,b,c)
    sumi=a+b+c
    print("YES") if sumi-maxi == maxi else print("NO")
    # print(maxi)
    # print(sumi)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(0, int(input())):
    a,b,c=map(int,input().split())
    maxi=max(a,b,c)
    sumi=a+b+c
    print("YES") if sumi-maxi == maxi else print("NO")
    # print(maxi)
    # print(sumi)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for t in range(int(input())):
    a,b,c = map(int,input().split())
    if((a==(b+c)) or (b==(a+c)) or (c==(b+a))):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        int a,b,c;
        cin>>a>>b>>c;
        if(a+b==c || a+c==b || c+b==a){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }

    }
}

