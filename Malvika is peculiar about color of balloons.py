#include <stdio.h>

int main(void) {
    int t;
	scanf("%d",&t);
	while(t--)
	{
	    char s[100],c=0,d=0;
	    scanf("%s",&s);
	    for(int i=0;i<strlen(s)+1;i++)
	    {
	        if(s[i]=='a')  
	            c+=1;
	        if(s[i]=='b')
	            d+=1;
	    }
	    if(c<=d)
	        printf("%d\n",c);
	    else
	        printf("%d\n",d);
	}
	return 0;
}









#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t){
	    string s;
	    // Taking input with the help of "cin" using the "extraction operator"
	    cin>>s;
	    int a=0,b=0;
	    for(char c:s){
	        if(c=='a'){
	            a++;
	        }
	        else{
	            b+=1;
	        }
	    }
	    cout<<((a>b)?b:a)<<endl;
	    t-=1;
	}
	return 0;
}



















for i in range(int(input())):
    s = input()
    a = s.count('a')
    b = s.count('b')
    if a==0 or b==0:
        print(0)
    else:
        print(min(a,b))