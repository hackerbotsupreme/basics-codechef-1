for i in range(int(input())):
    num=int(input())
    arr=list(map(int,input().split()))
    var=1
    for i in range(num):
        var*=arr[i]
    if(var<0):
        print(1)
    else:
        print(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        l=[]
        if 0 in k:
                print(0)
        else:
                for i in k:
                        if i<0:
                                l.append(i)
                print(0) if (len(l))%2==0 else print(1)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
/*
Observation 1: If the array has zero then the product will always be zero hence we dont need to do any operation
Observation 2: Negative numbers multiplied odd times results in a negative number whereas Negative numbers multiplied even times results in a positive number
Conclusion: If there exists one zero then we dont need to do anything.
            If number of negative numbers is even then we dont need to do anything
            If number of negative numebers is odd then we should delete one of them hence we need to do one operation
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int test_cases;
    cin >> test_cases;
    while(test_cases--){
        int n;
        cin >> n;
        vector<int> a(n);
        bool zero_found = false;
        int number_of_negative_numbers{0};
        for(int i = 0; i < n; i++){
            cin >> a[i];
            if(a[i] == 0){
                zero_found = true;
            } 
            if(a[i] < 0){
                number_of_negative_numbers++;
            }
        }
        if(zero_found){
            cout << 0 << '\n';
        } else{
            if(number_of_negative_numbers%2 == 0){
                cout << 0 << '\n';
            } else{
                cout << 1 << '\n';
            }
        }
    }
    return 0;
}

















#include <stdio.h>

int main(void) {
    int t,n;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
	    int zero=0,neg=0;
	scanf("%d",&n);
	int arr[n];
	for(int i=0;i<n;i++){
	    scanf("%d",&arr[i]);
	}
	for(int i=0;i<n;i++){
	  if(arr[i]==0){
	      zero++;
	  }
	  if(arr[i]<0){
	       neg++;
	      }
	}
	  if(zero>0||neg%2==0){
	      printf("\n0");
	  }
	  else{
	      printf("\n1");
	  }
}

	  return 0;
	}