import java.util.Scanner;

class TheCoolerDilemma2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();

        while (t != 0) {
            Long x = sc.nextLong();
            Long y = sc.nextLong();
                        
            if ( y % x != 0){
                System.out.println(y / x);
            }
            else{
                System.out.println((y/x)-1);
            }
            t--;
        }
    }

}










#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int x,y,d;
	    cin>>x>>y;
	    d=y/x;
	    if(d*x<y)
	    {
	        cout<<d<<endl;
	    }
	    else
	    cout<<d-1<<endl;
	}
	return 0;
}












#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {

int t;
cin>>t;

while(t>0){

int a,b,count;
cin>>a>>b;

count=b/a;

if(count*a<b){
cout<<count<<endl;
}
else{
cout<<count-1<<endl;
}
t--;
}
return 0;
}

