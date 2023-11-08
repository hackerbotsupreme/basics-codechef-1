found = {}
def byteLander(n):
    if n < 12:
        return n 
    elif n in found:
        return found[n]
    else:
        sum = byteLander(n//2) + byteLander(n//3) + byteLander(n//4)
        found[n] = sum
        return sum;

while True:
    try:
        n = int(input())
        print(byteLander(n))
    except:
        break

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

long solve(long n)
 {
    if(n>=12)
    return solve(n/2) + solve(n/3)+ solve( n/4);
    else
    return n;
    
}
int main() {
     long n; 
     while(cin>>n)
     cout<<solve(n)<<endl;
	
	return 0;
}














