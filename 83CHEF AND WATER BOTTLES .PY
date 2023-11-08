# cook your dish here
T= int(input())
for A in range(T):
    bottles=0
    N,X,K= map(int,input().split())
    if N*X<=K:
        print(N)
    else:
        for i in range(1,N+1):
            if X*i<=K:
                bottles= bottles+1
        print(bottles)
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    n,x,k=(map(int,input().split()))
    if(k//x<n):
        print(k//x)
    elif(k//x>n):
        print(n)
    else:
        print(0)
        
        
# cook your dish here
for i in range(int(input())):
    n,x,k=map(int,input().split())
    if(k//x<n):
        print(k//x)
    elif(k//x>n):
        print(n)
    else:
        print(0)
        
        
        
# cook your dis
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    s=k//x
    if s>=n:
       print(n)
        
    else:
        print(s)
        
        
        
