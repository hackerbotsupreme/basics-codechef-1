#include <iostream>
using namespace std;

int main() {

    int t;
    cin>>t;
    while(t--)
    {
        int n,k,x,y;
        cin>>n>>k>>x>>y;
        //cost of red  k*x
        //cost of blue n-k*y 
        //total cost = k*x + n-k*y 
        
        cout<<(k*x)+((n-k)*(min(x,y)))<<endl;
    }
	return 0;
}






#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,k,x,y;
	    cin>>n>>k>>x>>y;
	    int min=k*x;
	    int rem1=(n-k)*x;
	    int rem2=(n-k)*y;
	    if(rem1<=rem2)
	    {
	        cout<<rem1+min<<endl;
	    }
	    else
	    {
	        cout<<rem2+min<<endl;
	    }
	}
	return 0;
}









#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,k,x,y;
	    scanf("%d %d %d %d",&n,&k,&x,&y);
	    int temp;
	    temp= (k*x);
	    if(x>y)
	    temp=temp + (n-k)*y;
	    else
	    temp=temp + (n-k)*x;
	    
        printf("%d\n",temp);
	}
	return 0;
}










/*An electronics shop sells red and blue lamps. A red lamp costs X rupees and a blue lamp costs Y rupees.
Chef is going to buy exactly N lamps from this shop. Find the minimum amount of money Chef needs to pay such 
that at least K of the lamps bought are red.*/
#include<stdio.h>
int main()
{
    int Test_Cases;
    scanf("%d",&Test_Cases);
    while(Test_Cases--)
    {
        int Red_Lamp_Cost,Blue_Lamp_Cost,Required_Lamps,Required_Red_Lamps;
        scanf("%d%d%d%d",&Red_Lamp_Cost,&Blue_Lamp_Cost,&Required_Lamps,&Required_Red_Lamps);
        int Temp;
        Temp=Blue_Lamp_Cost*Required_Lamps;
        if(Required_Lamps>Required_Red_Lamps)
          Temp=Temp + (Red_Lamp_Cost - Blue_Lamp_Cost) * Required_Red_Lamps;
        else
          Temp=Temp+(Red_Lamp_Cost-Blue_Lamp_Cost)*Required_Lamps;
        printf("%d\n",Temp);  
    }
}