# cook your dish here
r,o,c=map(int,input().split())
print("YES") if ((20-o)*36+c>r) else print("NO")









#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {

int a,b,c;
cin>>a>>b>>c;

int count = 20 - b;
count = 36 * count;
count= c + count;

if(count>a){
cout<<"Yes"<<endl;    
} 
else{
cout<<"No"<<endl;    
}
return 0;
}











#include <bits/stdc++.h>
using namespace std;
int main()
{
    int r, o, c, remainingBall;
    scanf("%d %d %d", &r, &o, &c);

    remainingBall = (20 - o) * 6;
    r < c + (remainingBall * 6) ? printf("YES\n") : printf("NO\n");
    return 0;
}












#include <iostream>
using namespace std;

int main() {
	int r,o,c;
	cin >>r>>o>>c;
	if(c+(20-o)*36>r)
	cout <<"YES"<<endl;
	else
	cout <<"NO"<<endl;
	return 0;
}