for i in range(int(input())):
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c = 0
    at = a[0]
    
    for x in range(0, n):
        if x > 0:
            at = a[x] - a[x-1]
        if at >= b[x]:
            c += 1
    
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t=0;
	cin>>t;
	
	while(t--){
	    int n;
	    cin>>n;
	    
	    int a[n];
	    int b[n];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	        //cin>>b[i];
	    }
	    for(int i=0;i<n;i++){
	       
	        cin>>b[i];
	    }
	   
	    
	    int count=0;
	    for(int i=0;i<n;i++){
	        if(i==0 && (a[i]>=b[i])){
                count++;
            }
            else if (a[i]-a[i-1]>=b[i])
            {
                count++;
            }
	    }
	    cout<<count<<endl;
	}
	return 0;
}





























#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int N;
	    cin>>N;
	    int A[N], B[N];
	    for(int i=0;i<N;i++)
	        cin>>A[i];
	    for(int i=0;i<N;i++)
	        cin>>B[i];
	    int count =0;
	    for(int i=0;i<N;i++){
	        if(i==0){
	            if(B[i] <= A[i]-0 )
	                count++;
	        }
	        else{
	            if(B[i] <= (A[i]-A[i-1]))
	                count++;
	        }
	    }
	    cout<<count<<endl;
	}
	return 0;
}









