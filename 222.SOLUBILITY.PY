for _ in range(int(input())):
    x,a,b = map(int,input().split())
    ans1 = (a+(100-x)*b)*10
    print(ans1)
    
    
    
    
    
    
    
    
    
    
    
    
T=int(input())
for i in range(T):
    X,A,B=map(int,input().split())
    S=A+(100-X)*B
    print(S*10)
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        x,a,b=map(int,input().split())
        print((a+(100-x)*b)*10)
        
        
        
        
        
        
        
        
        
        
        
        
        
#include<iostream>

int main() 
{
    int t;
    std::cin>>t;
    while(t--)
    {
        int x,a,b;
        std::cin>>x>>a>>b;
        int to100Deg = 100 - x;
        int additionalSugar = b * to100Deg;
        int sugarPerMlin100Deg = a + additionalSugar;
        std::cout<<sugarPerMlin100Deg * 10 <<std::endl;

    }

    return 0;
}