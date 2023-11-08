# cook your dish here
import math
for _ in range(int(input())):
    A,B= map(int,input().split())
    LCM = math.lcm(A,B)
    GCD= math.gcd(A,B)
    print(GCD,LCM)
    
    
    
import math
k = int(input())
for i in range(k):
    a,b = map(int,input().split())
    
    l = math.lcm(a,b)
    g = math.gcd(a,b)
    print(g,l)
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int a, b, m, g;
	    cin>>a>>b;
	    m = min(a, b);
	    
	    for (int i=1; i<=m; i++) {
	        if (a%i==0 && b%i==0) {
	            g = i;
	        }
	    }
	    long l = (long(a)*long(b))/g;
	    cout<<g<<" "<<l<<endl;
	}
	return 0;
}




#include <iostream>
#include<numeric>
using namespace std;

int main() {
	// your code goes here
	int t;
	long long int a,b;
	std::cin >> t;
	while(t--)
	{
	    std::cin >> a>>b;
	    std::cout <<std::gcd(a,b)<<" "<<std::lcm(a,b)<< std::endl;
	}
	
	return 0;
}