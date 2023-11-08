# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print((x*z)-(x*y))
    
    
    
    
    
    
    
    
    
    
    
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print((x*z)-(x*y))
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        x,y,z=map(int,input().split())
        print((z*x)-(x*y))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int profits(int x ,int y,int z){
    int d = x*y;
    int e = x*z;
    return e-d;
}
int main() {
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    std::cout << profits(x,y,z) << std::endl;
	}
	return 0;
}