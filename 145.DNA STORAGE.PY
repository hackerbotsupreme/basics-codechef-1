# cook your dish here
n=int(input())
for i in range(1,n+1):
    a=int(input())
    z=""
    h=str(input())
    for j in range(0,a,2):
        if(h[j]+h[j+1]=="00"):
            z=z+"A"
        elif(h[j]+h[j+1]=="01"):
            z=z+"T"
        elif(h[j]+h[j+1]=="10"):
            z=z+"C"
        else:
            z=z+"G"
    print(z)
    
    
    
    
/*

Hello coder!!!

Welcome to my solution (hope its correct XD). I just wanted to tell you that  if 
you want a bit more explanation  about this problem then you can visit my github
repository where I have posted a brief explanation of answer. 

Feel free to check it out , if you feel that my code can be optimized then
please create a pull request to update the solution. So in that way it can be 
helpful for others too.

Thanks and happy coding :)

**my github repo link**
https://github.com/soniyash9000/Code_chef_Solutions

*/


#define ll long long
#define f(end) for(int i=0;i<end;i++)
#define e '\n'
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t,n;
	cin>>t;
	while(t--)
	{
        cin>>n;
        string s, temp=" ";
        cin>>s;
        for(int i=0;i<s.length();i+=2)
        {
            if(s[i]=='0' && s[i+1]=='0') temp+='A';
            else if(s[i]=='0' && s[i+1]=='1') temp+='T';
            else if(s[i]=='1' && s[i+1]=='0') temp+='C';
            else temp+='G';
        }
        cout<<temp<<e;
	}
	return 0;
}







#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    string s,ns;
	    cin>>s;
	    for(int i=1;i<=n;i+=2){
	        if(s[i-1]=='0' && s[i]=='0'){
	            ns=ns+"A";
	        }else if(s[i-1]=='0' && s[i]=='1'){
	            ns=ns+"T";
	        }else if(s[i-1]=='1' && s[i]=='0'){
	            ns=ns+"C";
	        }else if(s[i-1]=='1' && s[i]=='1'){
	            ns=ns+"G";
	       
	        }
	         
	    }cout<<ns<<endl;
	}
	return 0;
}







#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    int n, k=0;
	    string s, s2="";
	    cin>>n>>s;
	    
	    for (char i: s) {
	        s2 += i;
	        k++;
	        if (k==2) {
	            if (s2 == "00") cout<<"A";
	            if (s2 == "01") cout<<"T";
	            if (s2 == "10") cout<<"C";
	            if (s2 == "11") cout<<"G";
	            s2 = "";
	            k = 0;
	        }
	    }
	    cout<<endl;
	}
	return 0;
}










