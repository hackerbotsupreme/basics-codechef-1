# cook your dish here 
for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    if(w==x or w==y or w==z):
        print("YES")
    elif(w==x+y or w==y+z or w==x+z):
        print("YES")
    elif(w==x+y+z):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int a,b,c,w;
    cin>>w>>a>>b>>c;
    int d = b+a;
    int e = a+c;
    int f = c+b;
    int g = a+b+c;
    if(w==a || w==b || w==c || w==d || w==e || w==f || w==g)cout<<"YES\n";
    else cout<<"NO\n";
}

int main()
{
    int test;
    cin>>test;
    while(test--)solve();

    return 0;
}

















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int w,a,b,c;
	    cin >> w >> a>>b>>c;
	    if(w==a or w==b or w==c)
	    cout << "YES" << endl;
	    else if(((a+b) == w) or ((b+c)==w) or((c+a)==w) or (w==(a+b+c)))
	    cout << "YES" << endl;
	    else
	    cout << "NO" << endl;
	}
	return 0;
}













#include <stdio.h>

int main(void){
    int t;
    scanf("%d", &t);
    while(t!=0)
    {
        int w,x,y,z;
        scanf("%d %d %d %d", &w, &x, &y, &z);
        if(w==x || w==y || w==z || w==(x+y) || w==(y+z) || w==(x+z) || w==(x+y+z))
        {
            printf("yes \n");
        }
        else
        printf("no \n");
        t--;
    }
    return 0;
}
