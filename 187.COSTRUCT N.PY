for t in range(int(input())):
    n = int(input())
    print("No" if (n%7)%2 != 0 and n < 7 else "Yes")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        /*
        let h = n/7
        for all n > 7, n = 7*(h-1) + 2*y
                                h,y => integers
        */
        if((n%7)%2 != 0 && n<7){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
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
	
	while(t--) {
	    int n;
	    cin>>n;
	    
	    if (n%2 == 0 || n >= 7) cout<<"YES";
	    else cout<<"NO";
	    
	    cout<<endl;
	}
	return 0;
}
















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int n;
	    cin>>n;
	    
	    if (n%2 == 0 || n >= 7) cout<<"YES";
	    else cout<<"NO";
	    
	    cout<<endl;
	}
	return 0;
}