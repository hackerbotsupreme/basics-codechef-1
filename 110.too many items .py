# cook your dish hereff
for i in range(int(input())):
        n=int(input())
        if n%10==0:
                print(n//10)
        else:
                
                print((n//10)+1)
                
                
                
                
                
                
                
                
                
                
                
                
#include <iostream>
using namespace std;

int main() {
    int T;
    cin>>T;
    while(T--){
        int a;
        cin>>a;
        if(a%10==0){
            cout<<(a/10)<<endl;
        }
        else{
            cout<<(a/10)+1<<endl;
        }
            }
    
    
}






#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t, n, result;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        result = ceil((float)n / 10);
        printf("%d\n", result);
    }

    return 0;
}