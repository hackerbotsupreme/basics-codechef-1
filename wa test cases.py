for _testcase in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = input()
    x = []
    for i in range(n):
        if (b[i]) == '0':
            x.append(a[i])
            
    print(min(x))
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int s[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>s[i];
	    }
	    string v;
	    cin>>v;
	    int a=10000000000,x;
	    for(int i=0;i<v.length();i++)
	   {
	      if(v[i]=='0')
	      {
	          x=s[i];
	          a=min(a,x);
	      }
	   }
	   cout<<a<<endl;
	}
	return 0;
}

















#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int s[n], j, x = 100000;
        string v;
        for (int i = 0; i < n; i++)
            cin >> s[i];

        cin >> v;
        for (int i = 0; i < v.length(); i++)
        {
            if (v[i] == '0')
            {
                j = s[i];
                x = min(x, j);
            }
        }
        cout << x << endl;
    }
    return 0;
}