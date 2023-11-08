# cook your dish here
for i in range(int(input())):
        a,b,m=map(int,input().split())
        print(min(abs(a-b),(m-abs(a-b))))
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int a,b,c;
	    cin>>a>>b>>c;
	    int x=min(abs(a-b),abs(abs(a-b)-c));
	    cout<<x<<endl;
	}
	return 0;
}













#include<iostream>

int main() 
{
    int t;
    std::cin>>t;
    while(t--) 
    {
        int m, a, b;
        std::cin>>a>>b>>m;

        int abs = std::abs(a-b);
        if(std::abs(abs-m) < abs)  
        {
            std::cout<<std::abs(abs-m)<<std::endl;
        }
        else 
        {
            std::cout<<abs<<std::endl;;
        }


    }
    return 0;
}









#include<iostream>

int main() 
{
    int t;
    std::cin>>t;
    while(t--) 
    {
        int m, a, b;
        std::cin>>a>>b>>m;

        int abs = std::abs(a-b);
        if(std::abs(abs-m) < abs)  
        {
            std::cout<<std::abs(abs-m)<<std::endl;
        }
        else 
        {
            std::cout<<abs<<std::endl;;
        }


    }
    return 0;
}


















#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int a,b,m;
	    cin>>a>>b>>m;
	    int l=abs(b-a);
	    if(abs(l-m)<l){
	        cout<<abs(l-m)<<endl;
	    }
	    else{
	        cout<<l<<endl;
	    }
	    
	}
	return 0;
}