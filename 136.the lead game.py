n = int(input())
play1 = 0
play2 = 0
max1 = 0
max2 = 0
for _ in range(n):
    a,b = map(int,input().split())
    max1 += a
    max2 += b
    if max1>max2:
        play1 = max(play1,max1-max2)
    else:
        play2 = max(play2,max2-max1)
if play1>play2:
    print(1,play1)
else:
    print(2,play2)
    
    
    
    
    
    
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	    int n;//number of round .
	    
	    cin>>n;
	    int winner=0;
	    int player1=0,player2=0; //cumulative  scores of players .initially taken as 0.
	    
	    int lead=0;// maximum lead after every round .initially taken as 0.
	    
	    while(n--){
	        int p1,p2;
	        cin>>p1>>p2;
	        player1+=p1; // p1 is the score of that particular round .
	                        // player1 is the total score of that player .
	                        
	        player2+=p2;// p2 is the score of that particular round .
	                        // player2 is the total score of that player .
	                        
	        int x=abs(player1-player2);// calculating lead after every particular round.
	                                    // x is current lead .hence lead of current round.
	        if(x>lead){   //if current lead if greater than maximum lead .means the mamximum lead would be change . winner would also be updated.
	        
	            lead=x; // mamimum lead changed.
	            
	            player1>player2?winner=1:winner=2;//winner updated .
	        }
	    }
	    cout<<winner<<" "<<lead<<endl; // display output 
	
	return 0;
}











#include <stdio.h>
int main(void) {
	int n,i;
    scanf("%d",&n);
    int a[n],b[n],lead[n],win[n];
    for(i=0;i<n;i++)
    {
        scanf("%d%d",&a[i],&b[i]);
    }
    int sum1=0,sum2=0;
    for(i=0;i<n;i++)
    {
        sum1+=a[i];
        sum2+=b[i];
        if(sum1>sum2)
        {
            lead[i]=sum1-sum2;
            win[i]=1;
        }
        else{
            lead[i]=sum2-sum1;
            win[i]=2;
        }
 }
  int w=0,l=0;
 for(i=0;i<n;i++){
  if(l<=lead[i])
  {
   l=lead[i];
   w=win[i];
  }
 }
 printf("%d %d",w,l);
	return 0;
}









