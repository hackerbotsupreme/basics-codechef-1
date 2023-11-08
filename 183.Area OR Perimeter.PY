# cook your dish here
l=int(input())
b=int(input())
area = l*b 
peri = 2*(l+b) 
if(area<peri):
    print("Peri") 
    print(peri) 
elif(area>peri):
    print("Area")
    print(area) 
else:
    print("Eq")
    print(area)
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
L = int(input())
B = int(input())
Area = L *B
peri = 2 * (L+B)
if peri > Area:
  print("Peri")
  print(peri)
elif peri < Area:
  print("Area")
  print(Area)
else:
  print("Eq")
  print(Area)
  
  
  
  
  
  
  
  
  
  
  
  
  
#include <iostream>
using namespace std;

int main() {
    int l,b;
    cin>>l>>b;
    int area=l*b;
    int peri=2*(l+b);
    if(area>peri)
    cout<<"Area"<<endl<<area<<endl;
    else if(area<peri)
    cout<<"Peri"<<endl<<peri<<endl;
    else cout<<"Eq"<<endl<<area<<endl;
	// your code goes here
	return 0;
}
















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int l, b, x, y;
	cin>>l>>b;
	
	x = l*b;
	y = 2*(l+b);
	
	if (x>y) cout<<"Area\n"<<x;
	else if (x==y) cout<<"Eq\n"<<x;
	else cout<<"Peri\n"<<y;
	
	return 0;
}