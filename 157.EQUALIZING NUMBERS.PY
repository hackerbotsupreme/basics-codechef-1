for _testcase in range(int(input())):
    n,k = map(int,input().split())
    if n == k: print("yes")
    elif (abs(n-k))%2 == 0: print("YES")
    else: print("NO")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
	    int a, b;
	    cin >> a >> b;
	    if (abs(a - b) % 2 != 0) {
	        cout << "No" << endl;
	    } else {
	        cout << "Yes" << endl;
	    }
	}
	return 0;
}


















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int a,b,d;
	    cin>>a>>b;
	   if(abs(a-b)%2!=0)
	    cout<<"NO"<<endl;
	    else
	    cout<<"YES"<<endl;
	}
	return 0;
}
















#include <stdio.h>

int main(void) {
	// your code goes here
	int kaushal;
	scanf("%d",&kaushal);
	while(kaushal--){
	 int one,two;
     scanf("%d %d",&one,&two);
     int three = abs(one-two);
         if(three%2==0){
             printf("\n Yes");
         }else
         {
             printf("\n no");
         }
         
    
	}
	return 0;
}


