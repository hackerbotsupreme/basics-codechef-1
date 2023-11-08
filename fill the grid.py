# cook your dish here
for t in range(int(input())):
    n,m = map(int,input().split())
    if(n%2!= 0 and m%2!=0):
        print(n+m-1)
    elif(n%2!= 0 and m%2==0):
        print(m)
    elif(n%2== 0 and m%2!=0):
        print(n)
    else:
        print(0)
        
        
        
        
        
        
# cook your dish here
t = int(input())
for _ in range(t):
    line  = input()
    words = line.split()
    n = int(words[0])
    m = int(words[1])
    a = (n // 2) * (m // 2)
    print(n * m - a * 4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	while(T--){
	   int n,m;
	   cin>>n>>m;
	   if(n%2==0&&m%2==0)cout<<"0\n";
	   else if(n%2==1&&m%2==1)cout<<n+m-1<<endl;
	   else if(n%2==0)cout<<n<<endl;
	   else cout<<m<<endl;
	}
	return 0;
}
















#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
// #include <stdlib.h>
// #include <math.h>
using namespace std;

// efficient solution, reduced the checking loop, A me input ho chuka hai already, B me input lete lete simultaneously check kar liya, so B me input leke usko(new i/p) turant check karke streak update karenge
int main()
{
    int testcase;
    cin >> testcase;
    for (int testcase_variable = 0; testcase_variable < testcase; testcase_variable++)
    {
        int n,m;
        cin>>n>>m;
        if (n%2==0 && m%2==0)// both are even
        {
            cout<<0<<endl;
        }
        else if (n%2==0 && m%2==1)// n is even, m is odd
        {
            cout<<n<<endl;
        }
        else if (n%2==1 && m%2==0)// m is even, n is odd
        {
            cout<<m<<endl;
        }
        else{// both are odd
            cout<<n+m-1<<endl;
        }
    }
}