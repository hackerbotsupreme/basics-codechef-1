#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--) {
	    char a[3], x, y;
	    
	    for (int i=0; i<3; i++) cin>>a[i];
	    cin>>x>>y;
	    
	    if (a[0] == x || a[0] == y) cout<<a[0];
	    else if (a[1] == x || a[1] == y) cout<<a[1];
	    
	    cout<<endl;
	}
	return 0;
}













#include <stdio.h>

int main(void)
{
	int t;
	scanf("%d", &t);
	while(t--)
	{
	    char a, b, c;
	    scanf(" %c %c %c", &a, &b, &c);
	    char x, y;
	    scanf(" %c %c", &x, &y);
	    if(x == a || y == a)
	        printf("%c\n", a);
	    else
	        printf("%c\n", b);
	}
	return 0;
}
















#include <iostream>
using namespace std;

int main() {
	
	int t;
	cin >> t;
	
	while(t--)
	{
	    int n = 3,p,s;
	    char arr[n];
	    
	    for(int i = 0;i < n ; i++)
	    {
	        cin >> arr[i];
	    }
	    
      char x,y;
      cin >> x >> y;

      for(int i = 0;i < n ; i++)
	    {
          if(arr[i] == x)       p = i;
          else if(arr[i] == y)      s = i;
	    }
        
    if(p < s)   cout << arr[p] << endl;
    else        cout << arr[s] << endl;
  }
	
	return 0;
}

















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	std::cin >> t;
	while(t--)
	{
	    char first,second,third,x,y;
	    std::cin >> first>>second>>third;
	    std::cin >>x>>y;
	    
	    if(x==first || y==first)    std::cout << first << std::endl;
	    else    std::cout << second << std::endl;
	}
	return 0;
}