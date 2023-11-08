# cook your dish here
x,y=map(str,input().split())
if x=="R" or y=="R":
    print("R")
elif x=="B" or y=="B":
    print("B")
else:
    print("G")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
x,y=input().split()
if x=="R" and y=="R":
        print("R")
elif x=="R" and y=="B":
        print("R")
elif x=="R" and y=="G":
        print("R")
elif x=="B" and y=="B":
        print("B")
elif x=="B" and y=="R":
        print("R")
elif x=="B" and y=="G":
        print("B")
elif x=="G" and y=="G":
        print("G")
elif x=="G" and y=="B":
        print("B")
elif x=="G" and y=="R":
        print("R")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t={'R','B','G'}
a,b=map(str,input().split())
if(a=='R' and b=='B'):
    print('R')
elif(a=='B' and b=='G'):
    print('B')
elif(a=='R' and b=='G'):
    print('R')
elif(a=='B' and b=='R'):
    print('R')
elif(a=='G' and b=='B'):
    print('B')
elif(a=='G' and b=='R'):
    print('R')
elif(a=='R' and b=='R'):
    print('R')
elif(a=='B' and b=='B'):
    print('B')
else:
    print('G')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
        char a,b;
       cin>>a>>b;
       
        if(a==b) 
        cout<<a<<endl;
        else if(a=='G' && b =='B' || a=='B' && b=='G')
        cout<<"B"<<endl;
        else if(a=='R' && b=='B' || a=='B' && b == 'R')
        cout<<"R"<<endl;
        else if(a=='G' && b=='R' || a=='R' && b=='G')
        cout<<"R"<<endl;
        
	return 0;
}




















#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	char c,s;
	cin>>c>>s;
	/*string R="3";
	string B="2";
	string G="1";*/
	
	if((c=='G'&& s=='B') ||(c=='B' && s=='G')){
	    cout<<"B"<<endl;
	}
	else{
	    int z=max(c,s);
     	cout<<char(z)<<endl;
	}
	
	return 0;
}