# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if(x<=3):
        print(x*y)
    else:
        if(x%3==0):
            m=(int(x/3)-1)*z+(x*y)
            print(m)
        else:
            m=(int(x/3))*z+(x*y)
            print(m)
            
            
            
# cook your dish here
for i in range(int(input())):
    x,y,z = map(int,input().split())
    time=0
    count=0
    while x:
        if count==3:
            time = time+z
            count = 0
        time = time + y
        x = x-1
        count +=1
    print(time)
    
    
    
    
    
# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int,input().split())
    if x <= 3:
        print(x*y)
    else:
        if x%3 != 0:
            print(x*y + (x//3)*z)
        else:
            print(x*y + ((x//3)-1)*z)
            
            
            
            
            
# cook your dish here
t=int(input())
for i in range(t):
    
    x,y,z=map(int,input().split())
    a=x*y
    b=x//3
    if x%3==0:
        b-=1
        print(a+b*z)
    else:
        print(a+b*z)

        
        
        
        
        

#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x,y,z;
	    cin>>x>>y>>z;
	    if(x<=3){
	        cout<<(x*y)<<endl;
	    }
	    else if (x%3==0){
	        int n=(((x/3)-1)*z)+(x*y);
	        cout<<n<<endl;
	    }
	    else{
	        cout<<((x/3)*z)+(x*y)<<endl;
	    }
	}
	return 0;
}