
# cook your dish here
import math
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=math.pow(a,2)
    d=math.pow(b,2)
    q=c+d;
    w=abs(c-d)
    x=math.sqrt(q)
    y=math.sqrt(w)
    #print("%.5f"%float(y),round(x,4))
    print(round(y,4),round(x,4))
    
    
    
    
    
    
    
    
    
    
    
    
import math
for _ in range(int(input())):
    b,ls=map(int,input().split())
    c=math.pow(b,2)
    d=math.pow(ls,2)
    rsM=math.sqrt(c+d);
    rsm=math.sqrt(abs(c-d))
    print(round(rsm,4),round(rsM,4))
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int b,ls;
	    cin>>b>>ls;
	  
	   
	   cout<<sqrt(ls*ls-b*b)<<" "<<sqrt(ls*ls+b*b)<<endl;
	}
	return 0;
}














#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,b,ls;
	cin>>t;
	while(t--)
	{
	    cin>>b>>ls;
	    cout.setf(ios::fixed);
		cout<<setprecision(2)<<sqrt(abs(b*b - ls*ls))<<" "<<sqrt(b*b + ls*ls)<<"\n";
	}
	return 0;
}

















#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++){
	    float b, ls;
	    cin >> b >> ls;
	    
	    cout << sqrt(abs(b * b - ls * ls)) << " " << sqrt(b * b + ls * ls) << "\n";
	}
	
	return 0;
}