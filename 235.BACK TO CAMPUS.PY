# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%k==0:
        print(int(n/k))
    else:   
        print(int((n/k)+1))
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    N,K=map(int,input().split())
    print(N//K + (0 if N%K==0 else 1))
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
import math as m
for _ in range(int(input())):
    n,k = map(int, input().split())
    print(m.ceil(n/k))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
import math
for i in range(int(input())):
        n,k=map(int,input().split())
        print(math.ceil(n/k))