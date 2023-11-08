# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=a*b-sum(c)
    if d>0:
        print(d)
    else:
        print(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int n,X,s,sum = 0;
	    
	    scanf("%d %d\n",&n,&X);
	    int arr[n-1];
	    
	    for(int i=0;i < n-1;i++){
	        
	        scanf("%d ",&arr[i]);
	    
	    
	    
	        sum = sum + arr[i];
	    }
	    s = X*n - sum;
	    if(s <= 0)
	    printf("0 \n");
	    else
	    printf("%d \n",s);
	}
	return 0;
}





#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n,x;
	    cin>>n>>x;
	    int a[n];
	    for(int i=0;i<(n-1);i++){
	        cin>>a[i];
	    }
	    int sum=0;
	    for(int i=0;i<(n-1);i++){
	       sum=sum+a[i];
	    }
	    int z=(x*n)-sum;
	    if(z>0){
	        cout<<z<<endl;
	    }
	    else{
	        cout<<"0"<<endl;
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
	    int n, x, sum=0, c;
	    cin>>n>>x;
	    
	    for (int i=0; i<n-1; i++) {
	        int a;
	        cin>>a;
	        sum += a;
	    }
	    c = n*x - sum;
	    
	    cout<<(c<0 ? 0 : c)<<endl;
	}
	return 0;
}