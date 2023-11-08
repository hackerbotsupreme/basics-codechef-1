# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    D = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if D[i]>=1000:
            count = count+1
            continue
    print(count)
    
    
    
# cook your dish here
for t in range(int(input())):
    n = int(input())
    N = list(map(int,input().split()))
    m = [m for m in N if m<1000]
    print(n-len(m))
    
    
    
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()[:n]))
    x=0
    for i in l:
        if i>=1000:
            x+=1 
    print(x)
    
    
# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for j in a:
        if j>=1000:
            s+=1
    print(s)        
    
    
    
    
    
# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    D = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if D[i]>=1000:
            count = count+1
            continue
    print(count)
    