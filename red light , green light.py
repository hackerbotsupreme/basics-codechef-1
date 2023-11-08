# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    
    H=list(map(int,input().split(" ")))
    c=0
    
    for j in range(n):
        if(H[j] > k):
            c+=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
t=int(input())
for i in range(t):
    N,K=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i>K:
            c=c+1
    print(c)        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for j in range(N):
        if A[j] > K:
            count+=1
    print(count)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        a,b=map(int,input().split())
        l=list(map(int,input().split()))
        count=0
        for i in l:
                if i>b:
                        count+=1
        print(count)