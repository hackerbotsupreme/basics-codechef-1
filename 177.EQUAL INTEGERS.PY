# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x<y:
        print(y-x)
    else:
        if (x-y)%2==0:
            print((x-y)//2)
        else:
            print((x-y)//2+2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x<y:
        print(y-x)
    else:
        if (x-y)%2==0:
            print((x-y)//2)
        else:
            print((x-y)//2+2)
    
    
    
    
    
    
    
    
    
    
    
    

#include <iostream>
using namespace std;
int main() {
 int t,x,y,c=0;
 cin>>t;
 while(t--)
 {                                                                    
    cin>>x>>y;
   if(x==y)
   {
       cout<<"0"<<endl;
   }
   else if(x<y)
   {
       cout<<y-x<<endl;
   }
   if(x>y)
   {
       if((x-y)%2==0)
       {
           cout<<(x-y)/2<<endl;
       }
       else cout<<(((x-y+1))/2)+1<<endl;
   }
}
return 0;}













#include<iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int x , y;
        int count_x =0 , count_y =0;
        cin >> x >> y;
        if(x < y || x == y){
          cout << abs(x -  y) <<endl;
        }
        else if(y < x){
            if(x%2 != 0 && y%2 == 0 || y%2 != 0 && x%2 == 0){
                x = x+1 ;
                count_x++;
                do{
                    y= y+2 ; 
                    count_y++;
                }while(x != y);
            }
            else{
                 do{
                    y= y+2 ; 
                    count_y++;
                }while(x != y);
            }
            cout << count_x + count_y <<endl;
        }
    }
    return 0;
}