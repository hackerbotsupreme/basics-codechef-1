# cook your dish here
for i in range(int(input())):
    a,b,c=map(float,input().split())
    if(a>50 and b<0.7 and c>5600):
        print(10)
    elif(a>50 and b<0.7):
        print(9)
    elif(b<0.7 and c>5600):
        print(8)
    elif(a>50 and c>5600):
        print(7)
    elif(a>50 or b<0.7 or c>5600):
        print(6)
    else:
        print(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        h,c,t=map(float,input().split())
        if h>50 and c<0.7 and t>5600:
                print(10)
        elif h>50 and c<0.7 :
                print(9)
        elif c<0.7 and t>5600:
                print(8)
        elif h>50 and t>5600:
                print(7)
        elif h>50 or c<0.7 or t>5600:
                print(6)
        else:
                print(5)
                
                
                
                
                
                
                
                
                
                
# cook your dish here
for i in range(int(input())):
  h,c,t = map(float,input().split())
  if h>50 and c<0.7 and t>5600:
    print("10")
  elif h>50 and c<0.7:
    print("9")
  elif c<0.7 and t>5600:
    print("8")
  elif h>50 and t>5600:
    print("7")
  elif h>50 or c<0.7 or t>5600:
    print("6")
  else:
    print("5")
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int testcases;
	cin>>testcases;
	while(testcases--)
	{
	    float hardness,carboncontent,tensilestrength;
	    cin>>hardness>>carboncontent>>tensilestrength;
	    if(hardness>50 && carboncontent<0.7 && tensilestrength>5600)
	    {
	        cout<<"10"<<endl;
	    }
	    else
	    {
	        if(hardness>50 && carboncontent<0.70)
	        cout<<"9"<<endl;
	        else if(carboncontent<0.7 && tensilestrength>5600)
	        cout<<"8"<<endl;
	        else if(hardness>50 && tensilestrength>5600)
	        cout<<"7"<<endl;
	        else if(hardness>50 || carboncontent<0.7 || tensilestrength>5600)
	        cout<<"6"<<endl;
	        else 
	        cout<<"5"<<endl;
	    }
	}
	
	return 0;
}













#include <iostream>
using namespace std;

int main() {
	int t, hardness, Tstrength;
	float carbon;
	cin >> t;
	while(t--) {
	    cin >> hardness >> carbon >> Tstrength;
	    bool con1 = hardness>50;
	    bool con2 = carbon<0.7;
	    bool con3 = Tstrength>5600;
	    if(con1 && con2 && con3) cout << "10\n";
	    else if(con1 && con2) cout << "9\n";
	    else if(con2 && con3) cout << "8\n";
	    else if(con1 && con3) cout << "7\n";
	    else if((!con1) && (!con2) && (!con3)) cout << "5\n";
	    else cout << "6\n";
	}
	return 0;
}







