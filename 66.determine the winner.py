# cook your dish here
for i in range(int(input())):
    a,b,c,d = map(int, input().split(" "))
    maxa = max(a,b)
    maxb = max(c,d)
    if(maxa > maxb):
        print("Q")
    elif(maxa < maxb):
        print("P")
    if(maxa == maxb):
        print("TIE")
        
        
        
        
# cook your dish here

t=int(input())
for i in range(t):
    Pa,Pb,Qa,Qb=map(int,input().split())
    if Pa>Pb:
        r=Pa
    else:
        r=Pb
    if Qa>Qb:
        q=Qa
    else:
        q=Qb
    if r>q:
        print("Q")
    elif r==q :
        print("TIE")
    else:
        print("P")
        
        


#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t, pa, pb, qa, qb, x, y, z;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d %d %d", &pa, &pb, &qa, &qb);
        int max1 = max(pa, pb);
        int max2 = max(qa, qb);

        if (max1 > max2)
        {
            printf("Q\n");
        }
        else if (max1 < max2)
        {
            printf("P\n");
        }
        else
        {
            printf("TIE\n");
        }
    }

    return 0;
}





#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int p1,p2,q1,q2;
	    cin>>p1>>p2>>q1>>q2;
	    if(max(p1,p2)>max(q1,q2))
	    cout<<"Q"<<endl;
	    else if(max(p1,p2)<max(q1,q2))
	    cout<<"P"<<endl;
	    else
	    cout<<"TIE"<<endl;
	}
	return 0;
}