# cook your dish here
for I in range(int(input())):
    a,b,c=map(int,input().split())
    f=-1
    while(a):
        a//=2
        f+=1
    k=f*b+(f-1)*c
    print(k)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    c=0
    while n>1:
        c+=1 
        n=n/2
        
    print((c*a)+((c-1)*b))






import math

for i in range(int(input())):
    lst = list(map(int,input().strip().split()))
    print(round(math.log(lst[0],2))*(lst[1]+lst[2])-lst[2])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
T=int(input())
for o in range(T):
    N,A,B=map(int,input().split())
    c=0
    for i in range(N):
        N=N//2
        c+=1
        if N==1:
            break
    print((c*(A+B))-B)