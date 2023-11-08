from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(n-max(Counter(l).values()))
    
    
    
    
    
    
    
    
    
    
    
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(n-max(Counter(l).values()))
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
from statistics import mode
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(N- A.count(mode(A)))
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish h
for _ in range(int(input())):
    m=[]
    n=int(input())
    a=list(map(int,input().split(" ")))
    for i in a:
        s=a.count(i)
        m.append(s)
    print(n-max(m))
    

