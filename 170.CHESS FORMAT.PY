for _testcase in range(int(input())):
    a,b = map(int, input().split())
    if (a + b) < 3: print('1')
    elif 11 <= (a + b) <= 60  : print('3')
    elif 60 < (a + b): print('4')
    else: print('2')









# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    a=a+b
    if(a<3):
        print("1")
    elif(3<=a and a<=10):
        print("2")
    elif(11<=a and a<=60):
        print("3")
    else:
        print("4")
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  a,b = map(int,input().split())
  if a+b < 3:
    print("1")
  elif a+b>=3 and a+b<=10:
    print("2")
  elif a+b>=11 and a+b<=60:
    print("3")
  else:
    print("4")
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
    {
        int a,b;
        cin>>a>>b;
        if((a+b)<3)
        cout<<"1"<<endl;
        else if( (a + b)>=3 && (a + b)<=10)
        cout<<"2"<<endl;
        else if((a + b)>=11 && (a + b)<=60)
        cout<<"3"<<endl;
        else if(60<(a+b))
        cout<<"4"<<endl;
    }
	return 0;
}
        
        
        
        
        
        
        
        
        
        
        
        
