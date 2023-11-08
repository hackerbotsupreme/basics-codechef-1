n,h,x=map(int,input().split())
l=list(map(int,input().split()))
ans="NO"
for i in l:
    if i+x>=h:
        ans="YES"
        break 
print(ans)












# cook your dish here


n,h,x=map(int,input().split())
l=list(map(int,input().split()))
ans="NO"
for i in l:
    if i+x>=h:
        ans="YES"
        break 
print(ans)














N,H,x = map(int,input().split())
t = list(map(int,input().strip().split()))
count=0
for i in t:
    if (i+x)>=H:
        count+=1
    
if count>0:
    print("Yes")
else:
    print("No")
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	int n, h , x;
	cin>>n >> h >> x;
	int t[n];
	bool isPossible = false;
	for(int i=0; i<n; i++){
	    cin>>t[i];
	    if((x+t[i]) >= h ) isPossible = true;
	}
	
	isPossible ? cout<<"YES" : cout<<"NO";
	return 0;
}





#include <iostream>
using namespace std;

int main() {
	int n, h , x;
	cin>>n >> h >> x;
	int t[n];
	bool isPossible = false;
	for(int i=0; i<n; i++){
	    cin>>t[i];
	    if((x+t[i]) >= h ) isPossible = true;
	}
	
	isPossible ? cout<<"YES" : cout<<"NO";
	return 0;
}