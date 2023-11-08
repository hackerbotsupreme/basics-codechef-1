t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=b-a
    if ((c-2)%3)==0:
            print("no")
    else:
        print("yes")
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b;
	    cin>>a>>b;
	    int c=b-a;
	    if(c%3==0 || c%3==1){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
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
	while(t--){
	    int a,b;
	    cin>>a>>b;
	    int c=b-a;
	    if(c%3==0 || c%3==1){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}








#include <stdio.h>

int main(void) {
  // your code goes here
  int t;
  scanf("%d", &t);
  while (t--) {
    int a, b;
    scanf("%d %d", &a, &b);
    int diff = b - a;
    diff -= 2;
    if (diff % 3 == 0) {
      printf("NO\n");
    } else {
      printf("YES\n");
    }
  }
}