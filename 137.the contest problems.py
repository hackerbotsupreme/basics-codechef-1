# cook your dish here
for i in range(int(input())):
        n=int(input())
        l=list(input().split())
        a=0
        b=0
        for i in l:
                if i=="START38":
                       a+=1
                else:
                        b+=1
        print(a,b)
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,n;cin>>t;
	while(t--){
	    cin>>n;
	    string s;
	    int sum1 =0, sum2 =0;
	    while(n--){
	        cin>>s;
	        if(s[0] == 'S')sum1 += 1;
	        else sum2 += 1;
	    }
	    cout<<sum1<<" "<<sum2<<"\n";
	}
	return 0;
}












#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int cnt=0;
	    for(int i=0;i<n;i++){
	        string s;
	        cin>>s;
	        if(s=="START38"){
	            cnt++;
	        }
	    }
	    cout<<cnt<<" "<<n-cnt<<endl;
	}
	return 0;
}











#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
	    int j,c_1=0,c_2=0;
	    cin>>j;
	    //created a array type string
	    string arr[j];
	    for(int k=0;k<j;k++){
	        cin>>arr[k];
	    }
	    for(int k=0;k<j;k++){
	        if(arr[k]=="START38"){
	            c_1++;
	        }
	        else{
	            c_2++;
	        }
	    }
	    cout<<c_1<<" "<<c_2<<"\n";
	}
	return 0;
}        
        







