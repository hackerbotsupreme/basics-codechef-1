# cook your dish here
for _ in range(int(input())):
    X=int(input())
    s=input()
    c,n=0,0
    for i in s:
        if i=='C':
            c+=2
        elif i=='N':
            n+=2
        else:
            c+=1
            n+=1
    print(55*X if c==n else(60*X if c>n else 40*X))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    a=int(input()) 
    b=input("")
    x=b.count('C')
    y=b.count('N')
    z=b.count('D')
    c=((x*2)+(z*1))>(z*1)+(y*2) 
    if(c is True):
        print(60*a)
    elif(z+(x*2)==z+(y*2)):
        print(55*a)
    else:
        print(40*a)
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        n=int(input())
        s=input()
        if (((s.count("C"))*2+(s.count("D"))*1)>((s.count("N"))*2+(s.count("D"))*1)):
                print(60*n)
        elif (((s.count("C"))*2+(s.count("D"))*1)==((s.count("N"))*2+(s.count("D"))*1)):
                print(55*n) 
        else:
                print(40*n)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, x, c, n, d;
	string s;
	cin>>t;
	while(t--){
	    cin>>x;
	    cin>>s;
	    
	    c = 0, n = 0, d = 0;
	    for (int i = 0; i < 14; i++) {
	        if(s[i] == 'C'){
	            c++;
	        }
	        else if(s[i] == 'D'){
	            d++;
	        }
	        else if(s[i] == 'N'){
	            n++;
	        }
	    }
	    
	    if(c > n){
	        cout<<60*x<<endl;
	    }
	    else if(c == n){
	        cout<<55*x<<endl;
	    }
	    else{
	        cout<<40*x<<endl;
	    }
	}
	return 0;
}





















#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	if(t>=1 && t<=1000) {
	    while(t--) {
	        int x; cin >> x;
	        char arr[14];
	        for(int i=0; i<14; i++)
	        cin >> arr[i];
	        int p1=0, p2=0; int prize=0;
	        for(int i=0; i<14; i++){
	                if(arr[i]=='C') {
	                    p1=p1+2;
	                    p2+=0;
	                } //Carlsen wins
	                if(arr[i]=='N') {
	                    p2=p2+2;
	                    p1+=0;
	                } //Chef wins
	                if(arr[i]=='D') {
	                    p1+=1; p2+=1;
	                }
	            }
	            if(p1>p2) prize=60*x;
	        if(p1<p2) prize=40*x;
	        if(p1==p2) prize=55*x;
	        cout<<prize<<endl;
	    }
	}
	return 0;
}