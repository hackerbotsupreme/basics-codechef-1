# cook your dish here
n=int(input())
for i in range(n):
        a=list(map(int,input().split()))
        if sum(a)==0:
                print("Beginner")
        elif sum(a)==1:
                print("Junior Developer")
        elif sum(a)==2:
                print("Middle Developer")
        elif sum(a)==3:
                print("Senior Developer")
        elif sum(a)==4:
                print("Hacker")
        else:
                print("Jeff Dean")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int a[5];
	    int count=0;
	    for(int i=0;i<5;i++)
	    cin >> a[i];
	    for(int i=0 ;i<5;i++)
	    {
	        if(a[i]==1)
	        count++;
	    }
	    if(count == 0)
	    cout << "Beginner" << endl;
	    else if(count ==1)
	    cout <<"Junior Developer" << endl;
	    else if(count == 2)
	    cout << "Middle Developer" << endl;
	    else if(count == 3)
	    cout <<"Senior Developer" << endl;
	    else if(count ==4)
	    cout<<"Hacker"<<endl;
	    else
	    cout<<"Jeff Dean"<<endl;
	}
	return 0;
}
























#include <iostream>
using namespace std;

int main() {
    int t;cin>>t;
    int arr[5];
    while(t--)
    {
    int count=0;
        for(int i=0;i<5;i++)
        {
            cin>>arr[i];
            if(arr[i]==1)
            {
                count++;
            }
        }
        if(count==0)
        {
            cout<<"Beginner"<<endl;
        }
        else if(count==1)
        {
           cout<<"Junior Developer"<<endl;  
        }
         else if(count==2)
        {
           cout<<"Middle Developer"<<endl;  
        }
         else if(count==3)
        {
           cout<<"Senior Developer"<<endl;  
        }
         else if(count==4)
        {
           cout<<"Hacker"<<endl;  
        } else if(count==5)
        {
           cout<<"Jeff Dean"<<endl;  
        }
    }
	// your code goes here
	return 0;
}


