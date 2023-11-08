# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    a=c//a
    b=d//b
    print(a+b)
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
  xa,xb,Xa,Xb = map(int,input().split())
  print(int((Xa/xa)+(Xb/xb)))
  
  
  
  
  
  
  
  
  
# cook your dish here
for i in range(int(input())):
  xa,xb,Xa,Xb = map(int,input().split())
  print(int((Xa/xa)+(Xb/xb)))
  
  
  
  
  
  
  
  
  
  
  
#include <iostream>
using namespace std;

int main() {int t,a,b,c,d;
 cin>>t;
 while(t--)
 {
     cin>>a>>b>>c>>d;
     int one=c/a; 
     int two=d/b;
     int ans=one+two;
     cout<<ans<<endl;
 }
}