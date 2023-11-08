# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y <= z:
        print('YEs')
    else:
        print('No')
        
        
        
        
        
        
        
        
        
for t in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y <= z:
        print('YEs')
    else:
        print('No')
        
        
        
        
        
        
        
        
        
        
        
        
for t in range (int(input())):
    x, y, z = map(int, input().split())
    if(x + y <= z):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
ValueError



#include <iostream>
using namespace std;

bool check (int x,int y,int z){
    if((x+y)<=z){
    return true;
    }
    return false;
}
int main() {
     int t;
     cin>>t;
     while(t--){
         int x,y,z;
         cin>>x>>y>>z;
         check(x,y,z) ? cout<<"YES"<<endl : cout<<"NO"<<endl;
     }
	return 0;
}