#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;cin>>t;while(t--)
	{
	    int n;cin>>n; int a[n]; int sum=0;
	       for(int i=0;i<n;i++)
	       {
	          cin>>a[i];
	           sum=sum+a[i];
	       }
	       if (n%2==0)
	       {cout<<abs(sum)/2<<endl;}
	       else
	       cout<<"-1"<<endl;
	}   
	return 0;
}










#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {

int t;
cin>>t;

while(t>0){

int n,sum=0,num=0;
cin>>n;

int arr[n];
for(int i=0;i<n;i++){
cin>>arr[i];
}
for(int i = 0; i < n; i++)
{
sum=sum + arr[i];
}

if(num+sum==0){
cout<<0<<endl;    
}
else if((sum)%2==0){
cout<<abs(sum)/2<<endl;;    
}
else{
cout<<-1<<endl;   
}
t--;
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
	    int a[n];
	    int count=0;
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	    }
	    if(n%2!=0){
	        cout<<"-1"<<endl;
	    }
	    else{
	        for(int i=0;i<n;i++){
	        if(a[i]==1){
	            count++;
	        }
	    }
	    cout<<abs((n/2)-count)<<endl;
	    }
	}
	return 0;
}














#include <iostream>
using namespace std;

int main() {
	// your code goes here
	
	int t,n;
	std::cin >> t;
	while(t-- )
	{
	    std::cin >> n;
	    int a[n],count;
	        int pos=0,neg=0;
	    for (int i = 0; i < n; i++) {
	        /* code */
	        std::cin >> a[i];
	        if(n%2==0) 
	        {
	            if(a[i]>0)
	            {
	                pos++;
	            }
	            else{
	                neg++;
	            }
	        }
	    }
	     if(n%2!=0) std::cout << -1 << std::endl; 
	    else if(pos>neg)    std::cout << pos-n/2 << std::endl;
	    else   std::cout << neg-n/2 << std::endl;
	   
	}
	return 0;
}