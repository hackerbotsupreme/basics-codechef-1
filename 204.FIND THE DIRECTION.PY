#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,c=0;
        cin>>n;
        string s;
        cin>>s;
        for(int i=0;i<n;i++)
        {
            if(s[i]==s[i+1])
            {
                c++;
            }
        }
        cout<<c<<endl;
    }
	return 0;
}










T = int(input())
for t in range(T):
    X=int(input())

    if X%4==0:
        print('North')
    elif X%4==1:
        print('East')
    elif X%4==2:
        print('South')
    elif X%4==3:
        print('West')
    else:
        continue
    
    
    
    
    
    
    
    
    
    
for t in range(int(input())):
    x = int(input())
    if(x%4==0):
        print("North")
    elif(x%4==1):
        print("East")
    elif(x%4==2):
        print("South")
    elif(x%4==3):
        print("West")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int s,count = 0;
        cin>>s;
        for(int i = 0; i < s; i++){
            if(count == 4){
                count = 0;
            }
            count++;
        }
        if(count == 1) cout<<"East"<<endl;
        else if(count == 2) cout<<"South"<<endl;
        else if(count == 3) cout<<"West"<<endl;
        else cout<<"North"<<endl;
    }
    return 0;
}

















#include <stdio.h>

int main(void) {
int n;
scanf("%d",&n);
while(n--)
{
    int a;
    scanf("%d",&a);
    if(a%4==0)
    {
        printf("North\n");
    }else if(a%4==1)
    {
        printf("East\n");
    }else if(a%4==2)
    {
        printf("South\n");
    }else
    {
        printf("West\n");
    }
}    
	return 0;
}
