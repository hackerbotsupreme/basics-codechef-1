# cook your dish here
c=input()
print("Vowel") if c in ['A','E','I','O','U'] else print("Consonant")











# cook your dish here
C = input()
l = ['A','E','I','O','U']
if C in l:
  print("Vowel")
else:
  print("Consonant")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	char a;
	std::cin >> a;
	std::array<int, 5> arr ={'A','E','I','O','U'} ;
	if(binary_search(arr.begin(),arr.end(),a))
	std::cout << "Vowel" << std::endl;
	else
	std::cout << "Consonant" << std::endl;
	return 0;
}













#include <iostream>
using namespace std;

int main()
{
        char a;
	    cin>>a;
	    if(a=='A' || a=='E' || a=='I' || a=='O' || a=='U')
	    cout<<"Vowel"<<endl;
	    else
	    cout<<"Consonant"<<endl;
	return 0;
}