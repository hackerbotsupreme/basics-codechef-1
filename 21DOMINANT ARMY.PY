for t in range(int(input())):
    na,nb,nc = map(int,input().split())
    c = 0
    if(na>(nc+nb)):
        c = 1 
    elif(nb>(nc+na)):
        c = 1 
    elif(nc>(na+nb)):
        c = 1 
    if(c==1):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a>b+c):
        print("YES")
    elif(b>a+c):
        print("YES") 
    elif(c>a+b):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    na,nb,nc=map(int,input().split())
    if na>nb:
        if na>nc:
            if na>nb+nc:
                print("YES")
            else:
                print("NO")
        else:
            if nc>na+nb:
                print("YES")
            else:
                print("NO")
    else:
        if nb>nc:
            if nb>na+nc:
                print("YES")
            else:
                print("NO")
        else:
            if nc>na+nb:
                print("YES")
            else:
                print("NO")













# cook your dish here

for _ in range(int(input())):
    A,B,C = map(int,input().split())
    if A > B + C:
        print('yes')
    elif B > A + C:
        print('yes')
    elif C > A + B:
        print('yes')
    else:
        print('no')
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	int t,a,b,c;
	cin>>t;
	while(t--){
	    cin>>a>>b>>c;
	    if((a+b)<c ||(b+c)<a ||(a+c)<b ){
	        cout<<"yes"<<endl;
	}else{
	    cout<<"no"<<endl;
	}
	}
	return 0;
}