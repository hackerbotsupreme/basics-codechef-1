#include <iostream>
#include<cmath>
using namespace std;

void chkPrime(int n){
    bool isPrime = true;
    if(n<2){
        isPrime = false;
    }
    for(int i = 2; i <= sqrt(n); i++){
        if(n%i == 0){
            isPrime = false;
        }
    }
    if(isPrime){
        cout<<"yes"<<endl;
    } else{
        cout<<"no"<<endl;
    }
}

int main() {
	// your code 
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        chkPrime(n);
    }
	return 0;
}










#include<stdio.h>
int main()
{
    int Test_Cases;
    scanf("%d",&Test_Cases);
    while(Test_Cases--)
    {
        int  a,b,c=0;
    scanf("%d",&a);
    for(b=1;b<=a;b++)
      {
        if(a%b==0)
        {
            c++;
        }
      }
    if(c==2)
      printf("yes\n");
    else
      printf("no\n");
    }
    return 0;
}













#include <iostream>
#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main() {

int t;
cin>>t;

while(t>0){

int n;
cin>>n;


bool isPrime = true;

if(n<2){
isPrime = false;
}
for(int i = 2; i <= sqrt(n); i++){

if(n%i == 0){
isPrime = false;
}

}

if(isPrime){
cout<<"yes"<<endl;
} 

else{
cout<<"no"<<endl;
}

t--;
}
return 0;
}





#include <iostream>
using namespace std;
// #include<cmath>

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int count=0;
      
        for(int i=1;i<=n;i++){
            if(n%i==0)
                count++;
        }
        count!=2? cout<<"no\n" :cout<<"yes\n";
    }

	
}
