# cook your dish here
for i in range(int(input())):
    n = int(input())
    string = input()
    new_str = ''
    for i in range(n):
        if string[i]=='A':
            new_str = new_str + "T"
        elif string[i]=='T':
            new_str = new_str + "A"
        elif string[i]=='C':
            new_str = new_str + "G"
        elif string[i]=='G':
            new_str = new_str + "C"
    print(new_str)
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here	int t;
	int t;
	cin>>t;
	while(t--){
	  int n;
	  cin>>n;
	  string s;
	  cin>>s;
	  for(int i=0; i<n; i++){
	      if(s[i]=='A')
	      s[i]='T';
	      else if(s[i]=='T')
	      s[i]='A';
	      else if(s[i]=='C')
	      s[i]='G';
	      else if(s[i]=='G')
	      s[i]='C';
	  }
	  cout<<s<<endl;
	}
	return 0;
}




#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		char a[n];
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
		
			if(a[i]=='A')
				a[i]='T';			
			else if(a[i]=='T')
				a[i]='A';
								
			else if(a[i]=='C')
				a[i]='G';
			else if(a[i]=='G')
				a[i]='C';
		}
		for(int i=0;i<n;i++)
			cout<<a[i];
			
		cout<<endl;
	}
	
	return 0;
}





#include <iostream>
using namespace std;

int main() {
	// A=T,T=A,C=G, G=C 
	
	int t;
	std::cin >> t;
	while(t--)
	{
	    int n;
	std::cin >>n;
	char s[n];
	for (int i = 0; i < n; i++) {
	    /* code */
	    std::cin >> s[i];
	    
	    if(s[i]=='A')
	        s[i]='T';
	    
	    else if(s[i]=='T')
	        s[i]='A';
	    
	    else if(s[i]=='C')
	        s[i]='G';
	    
	    else
	        s[i]='C';
	  
	}
	
	    for (int i = 0; i < n; i++) {
	        /* code */
	        std::cout << s[i];
	        
	    }
	    std::cout << std::endl;

	
	}
	return 0;
}