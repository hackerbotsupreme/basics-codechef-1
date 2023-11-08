# cook your dish here
T=int(input())
for i in range(T):
    A,B,X,Y=map(int,input().split())
    if(A/X<B/Y):
         print("Chef")
    elif(A/X>B/Y):
         print("Chefina")
    else:
         print("Both")
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
# cook your dish here
for i in range(int(input())):
        a,b,x,y=map(int,input().split())
        if(a/b<x/y):
                print("Chef")
        elif(a/b>x/y):
                print("Chefina")
        else:
                print("Both")
                
                
                
                
                
                
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    double a,b,x,y;
	    cin>>a>>b>>x>>y;
	    if(a/x>b/y)
	    cout<<"Chefina"<<endl;
	    else if(a/x<b/y)
	    cout<<"Chef"<<endl;
	    else
	    cout<<"Both"<<endl;
	}
	return 0;
}












/*Two friends Chef and Chefina are currently on floors AA and BB respectively. They hear an
announcement that prizes are being distributed on the ground floor and so decide to
reach the ground floor as soon as possible.
Chef can climb down XX floors per minute while Chefina can climb down YY floors per
minute. Determine who will reach the ground floor first. In case both reach the ground
floor together, print Both.*/
#include <stdio.h>
int main()
{
    int testcases;
    scanf("%d", &testcases);
    while (testcases--)
    {
        float first_person_floor, second_person_floor, first_person_speed, second_person_speed;
        scanf("%f%f%f%f", &first_person_floor, &second_person_floor, &first_person_speed, &second_person_speed);
        float c = first_person_floor / first_person_speed;
        float d = second_person_floor/ second_person_speed;
        if (c > d)
            printf("Chefina\n");
        if (c < d)
            printf("Chef\n");
        if (c == d)
            printf("Both\n");
    }
}







/*Two friends Chef and Chefina are currently on floors AA and BB respectively. They hear an
announcement that prizes are being distributed on the ground floor and so decide to
reach the ground floor as soon as possible.
Chef can climb down XX floors per minute while Chefina can climb down YY floors per
minute. Determine who will reach the ground floor first. In case both reach the ground
floor together, print Both.*/
#include <stdio.h>
int main()
{
    int testcases;
    scanf("%d", &testcases);
    while (testcases--)
    {
        float first_person_floor, second_person_floor, first_person_speed, second_person_speed;
        scanf("%f%f%f%f", &first_person_floor, &second_person_floor, &first_person_speed, &second_person_speed);
        float c = first_person_floor / first_person_speed;
        float d = second_person_floor/ second_person_speed;
        if (c > d)
            printf("Chefina\n");
        if (c < d)
            printf("Chef\n");
        if (c == d)
            printf("Both\n");
    }
}
         
         
         
         
         
         
