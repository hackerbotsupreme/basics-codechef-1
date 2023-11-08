for testcases in range(int(input())):
    a,b,x,y=map(int,input().split())
    if(a>b):
        need=a-b 
        if(y>=need):print("YES")
        else: print("NO")
    elif b>a :
        need=b-a 
        if(x>=need): print("YES")
        else: print("NO")
    else : print("YES")
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(a<=b):
        if(b-a<=c):
            print("Yes")
        else:
            print("No")
    else:
        if(a-b<=d):
            print("Yes")
        else:
            print("No")
            
            
            
            
            
            
            
            
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	 while(t--){
	     
	     int a,b,x,y;
	     cin >> a >> b >> x >> y;
	     if(a<=b){
	         if((a+x)>=b){
	             cout << "YES" << endl;
	         }
	         else{
	             cout << "NO" << endl;
	         }
	     }
	     else if(a>b){
	         if((a-y)<=b){
	             cout << "YES" << endl;
	         }
	         else{
	             cout << "NO" << endl;
	         }
	     
	     }
	     
	     
	     
	     
	 }
	return 0;
}













#include <stdio.h>

int main(void) {
	// your code goes here
	int a,b,c,d,e;
	scanf("%d",&a);
	while(a--){
	    scanf("%d %d %d %d",&b,&c,&d,&e);
	    if(b == c){
	        printf("YES\n");
	    }
	    else if(b>c && (b-c <= e)){
	        printf("YES\n");
	    }
	    else if(c>b && c-b <= d){
	        printf("YES\n");
	    }
	    else {
	        printf("NO\n");
	    }
	}
	return 0;
}
















#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int dt;
	cin>>dt;
	while(dt--)
	{
	    int da,db,dx,dy;
	    cin>>da>>db>>dx>>dy;
	    int dd = abs(da-db);
	    cout<<((da>db)?((da-dy<=db)? "YES" : "NO") : (da<db)?((da+dx>=db)? "YES" : "NO"): "YES") <<endl;
	}
	return 0;
}



