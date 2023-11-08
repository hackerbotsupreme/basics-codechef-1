# cook your dish here
t=int(input())
for i in range(t):
    n=input()
    for i in range(0,len(n),2):
        if n[i]==n[i+1]:
            print("no")
            break 
    else:
        print("yes")
        
        
        
        
        
t=int(input())
while(t):
    log=input()
    size=len(log)
    for i in range(0,size,2):
        if(log[i]==log[i+1]):
            print("no")
            break
    else:
        print("yes")
    t-=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
#include<climits>
using namespace std;

//#define int long long
#define vi vector<int>
#define pii pair<int,int>
#define vii vector<pii>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define ff first
#define ss second
#define setBits(x) builtin_popcount(x)

int main() {
	// your code goes here
	int test;
	cin>>test;
	while(test--){
	    int flag=1;
	    string s;
	    cin>>s;
	    for(int i=0;i<s.size();i++){
	        if(s[i]==s[i+1]){
	            if(i%2==0 && (i+1)%2!=0){
	                flag=0;
	            
	            }
	            else{
	                continue;
	            }
	        }
	        
	    }
	    
	   // cout<<flag<<endl;
	    
	    if(flag==1){
	        cout<<"yes"<<endl;
	        
	    }
	    else if(flag==0){
	        cout<<"no"<<endl;
	        
	    }
	    
	}
	return 0;
}











