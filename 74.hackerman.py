prime=[1,2,3,5,7,11]
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    add=a+b
    if add in prime:
        print("Alice")
    else:
        print('Bob')
 


# cook your dish here
def fun(n):
    for I in range(2,int(n**0.5)+1):
        if(n%I==0):
            return False
    else:
        return True
for I in range(int(input())):
    m,n=map(int,input().split())
    if(fun(m+n)):
        print("Alice")
    else:
        print("Bob")
        
        
        
# cook your dish here
def checkPrime(x):
    c=0
    for i in range(1,x+1):
        if (x%i==0):
            c+=1
    if c==2:
        return 1
    else:
        return 0


t = int(input()) #Test Case
while (t<1 or t>36):
    t = int(input()) #Test Case

for _ in range(t):
    strNum=input().split()
    a = int(strNum[0])
    b = int(strNum[1])
    while (a<1 or a>6 or b<1 or b>6):
        strNum=input().split()
        a = int(strNum[0])
        b = int(strNum[1])
    if (checkPrime(a+b)==1):
        print("Alice")
    else:
        print("Bob")
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int x, y, s;
	    cin>>x>>y;
	    string k = "Alice";
	    s = x+y;
	    
	    for (int i=2; i<s; i++) {
	        if (s%i == 0) {
	            k = "Bob";
	            break;
	        }
	    }
	    cout<<k<<endl;
	}
	return 0;
}