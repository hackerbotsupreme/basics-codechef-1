#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    cout<<(n%5)+(n/5)*4<<endl;
	
	}
	return 0;
}







#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);
    while(t!=0)
    {
        int n;
        scanf("%d", &n);
         printf("%d \n",(n-(n/5)));
        t--;
    }
	// your code goes here
	return 0;
}











#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int ans=0;
	    int x=0;
	    if(n%5==0){
	      ///  x=(n/5);
	        cout<<(n-(n/5))<<endl;
	    }else{
	        ans=(n%5);
	        cout<<((n/5)*(4)+(ans))<<endl;
	    }
	}
	return 0;
}











/*Chef has fallen in love with Cheffina, and wants to buy NN gifts for her. On
reaching the gift shop, Chef got to know the following two things:
The cost of each gift is 11 coin.
On the purchase of every 4^{th}4
gift, Chef gets the 5^{th}5
What is the minimum number of coins that Chef will require in order to come out of the shop carrying NN gifts?*/
#include<stdio.h>
int main()
{
    int Test_Cases;
    scanf("%d",&Test_Cases);
    while (Test_Cases--)
    {
        int Number_Of_Gifts;
        scanf("%d",&Number_Of_Gifts);
        printf("%d\n",(Number_Of_Gifts-(Number_Of_Gifts/5)));
    }
    
}