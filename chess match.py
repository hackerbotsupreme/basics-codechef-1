#include <iostream>
using namespace std;

int chess(int n,int a,int b){
    int c=2*(180+n);
    int d=a+b;
    int e=c-d;
    
    return e;
}
int main() {
	int t;
	cin>>t;
	while(t--){
	    int n,a,b;
	    cin>>n>>a>>b;
	    std::cout << chess(n,a,b) << std::endl;
	}
	return 0;
}












#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int tc;
	cin>>tc;
	while(tc--){
	    int a,b,c;
	    cin>>a>>b>>c;
	    cout<<((2*(180 + a))-(c+b))<<endl;
	}
	return 0;
}
















#include <stdio.h>

int main(void) {
        int T;
        scanf("%d",&T);
        for(int i=0;i<T;i++)
        {
            int N,A,B;
            scanf("%d%d%d",&N,&A,&B);
            printf("%d\n",(2*(180+N))-(A+B));
        }
        	return 0;
}
