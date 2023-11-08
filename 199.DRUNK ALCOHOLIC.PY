for t in range(int(input())):
    c = 0
    for i in range(int(input())):
        if i%2 == 0:
            c+=3
        else:
            c-=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for t in range(int(input())):
    c = 0
    for i in range(int(input())):
        if i%2 == 0:
            c+=3
        else:
            c-=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
	    int K;
	    cin>>K;
	    if (K%2 == 0) {
	        cout<<K<<endl;
	    }
	    else {
	        cout<<K+2<<endl;
	    }
	}
	return 0;
}












#include<iostream>

int main() 
{
    int t;
    std::cin>>t;
    while(t--) 
    {
        int x, a, b;
        std::cin>>x;
        if(x % 2 != 0) 
        {
            a = ((x / 2) + 1) * 3;
            b = (x/2) ;
        }
        else 
        {
            a = (x/2) * 3;
            b = (x/2);
        }

        std::cout<<std::abs(a-b)<<std::endl;
    }
    return 0;
}