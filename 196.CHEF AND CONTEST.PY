for t in range(int(input())):
    x, y, p, q = map(int, input().split())
    if(y + (q * 10) < x + (p * 10)):
        print("Chefina")
    elif(x + (p * 10) < y + (q * 10)):
        print("Chef")
    else:
        print("Draw")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        x,y,p,q=map(int,input().split())
        if x+p*10 <y+q*10:
                print("Chef")
        elif x+p*10 >y+q*10:
                print("Chefina")
        else:
                print("Draw")
                
                
                
                
                
                
                
                
                
                
                
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;
	    int chef=(a+(c*10));
	    int chefina=(b+(d*10));
	    if(chef<chefina) cout<<"Chef"<<endl;
	    else if(chefina <chef) cout<<"Chefina"<<endl;
	    else cout<<"Draw"<<endl;
	}
	return 0;
}














#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;
	    int chef=(a+(c*10));
	    int chefina=(b+(d*10));
	    if(chef<chefina) cout<<"Chef"<<endl;
	    else if(chefina <chef) cout<<"Chefina"<<endl;
	    else cout<<"Draw"<<endl;
	}
	return 0;
}
                
