# cook your dish here
a=[10,5]
for i in range(int(input())):
    n=int(input())
    b=0
    for j in range(2):
        if(a[j]<=n):
            b=b+(n//a[j])
            n=n%a[j]
    
    if(n==0):
        print(b)
    else:
        print(-1)
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    x=int(input())
    if(x%10==0):
        print(x//10)
    elif(x%10!=0 and x%5==0):
        print((x//10)+1)
    else:
        print("-1")
        
        
        
        
        
        
        
        
        
        
        
        
        

#include <stdio.h>

int main(void){
int t;
scanf("%d",&t);
while(t--){
    int x;
    scanf("%d",&x);
    if(x%10==0){
        
        printf("%d\n",x/10);}
   else if(x%10!=0){
       if(x%5==0){
           printf("%d\n",(x/10)+(x%10)/5);
       }
   else{
   
       printf("-1\n");
   }}
    
    
}
	return 0;
}






#include <iostream>
using namespace std;

void fast(){
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
}

void solve()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x;
        cin>>x;
        int cnt{0};
        int arr[2] = {10,5};
        for(int i=0;i<2;i++)
        {
            cnt+=x/arr[i];
            x-=(arr[i]*(x/arr[i]));
        }
        cout<<((x)?-1:cnt)<<endl;
    }
}

int main() {
	fast();
	solve();
	return 0;
}


















#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    if(x%10==0){
	        cout<<x/10<<'\n';
	    }
	    else if(x%5==0){
	        cout<<x/10+1<<'\n';
	    }
	    else{
	        cout<<-1<<'\n';
	    }
	}
	return 0;
}