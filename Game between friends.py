# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    for i in range(2):
        if(a>=b):
            b+=c
            c=d
        else:
            a+=c
            c=d
    if(a>=b):
        print('N')
    else:print('S')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
t=int(input())
while(t):
    
    n,s,r,satya=map(int,input().split())
    
    # Firstly check which player will ritik give his coins to?
    if(n>=s):
        # Sobhagya is losing
        s+=r
    else:
        # Nitin is losing
        n+=r
        
    # Now check which player will Satya give his coins to?
    if(n>=s):
        # Sobhagya is losing
        s+=satya
    else:
        # Nitin is losing
        n+=satya
        
    # Now finally check after everything which player is winning?
    print("N") if(n>=s) else print("S")
    t-=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        if(a>=b){
            b=b+c;
        }
        else {
            a=a+c;
        }
        if(a>=b){
            b=b+d;
        }
        else{
            a=a+d;
        }
        if(a>=b){
            cout<<"N"<<endl;
    }
    else{
        cout<<"S"<<endl;
    }
}
}