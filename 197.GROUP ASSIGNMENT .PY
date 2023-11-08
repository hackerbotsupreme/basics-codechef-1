#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	std::cin >> t;
	while(t--){
	    int n,x;
	    std::cin >> n >> x;
	    std::cout << (2*n+1)-x << std::endl;
	}
	return 0;
}


















#include<iostream>

int main ()
{
    int t;
    std::cin>>t;
    while(t--) 
    {
        long long n,x;
        std::cin>>n>>x;
        int total_student = 2*n;
        std::cout<<total_student-(x-1)<<std::endl;
        
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
        int n, x;
        scanf("%d %d", &n, &x);
        printf("%d\n", (n * 2) - x + 1);
    }
	return 0;
}

/*

n = 5 * 2 = 10
7

*/