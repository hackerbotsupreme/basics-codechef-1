t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)
    b_max = max(b)
    for i in range(n):
        if a[i] == a_max:
            t_a = i
        #sum_a += a[i]
    for i in range(n):
        if b[i] == b_max:
            t_b = i
        #sum_b += b[i]
    sum_a = sum(a)-a[t_a]
    sum_b = sum(b)-b[t_b]
    if sum_a > sum_b:
        print('Bob')
    elif sum_a < sum_b:
        print('Alice')
    else: print('Draw')
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    a=sum(arr)-max(arr)
    bs=sum(arr1)-max(arr1)
    if(a>bs):
        print("Bob")
    elif(a==bs):
        print("Draw")
    else:
        print("Alice")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
	int T;
	cin >> T;
	while (T--){
	    int N;
	    cin >> N;
	    int A,B,Amax=0,Bmax=0,Atot=0,Btot=0;
	    for (int i =0 ; i<N; ++i) {
	        cin >>A;
	        Atot +=A;
	        Amax = max(A,Amax);
	    };
	    Atot -= Amax;
	    for (int i =0 ; i<N; ++i) {
	        cin >>B;
	        Btot +=B;
	        Bmax = max(B,Bmax);
	    };
	    Btot -= Bmax;
	    cout <<((Atot<Btot)?"Alice\n":(Atot>Btot)?"Bob\n":"Draw\n");
	}
	return 0;
}