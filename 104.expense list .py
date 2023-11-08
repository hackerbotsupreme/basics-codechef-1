import sys
for _ in range(int(sys.stdin.readline())):
    n,x=map(int,sys.stdin.readline().split())
    sys.stdout.write(str(2**(x-n))+'\n')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    amount=2**x 
    for i in range(n):
        per=(50/100)*amount
        amount-=per
    print(int(amount))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b = map(int, input().split())
    e = 2**b
    
    for i in range(1,a+1):
        e -= e/2
        
    print(int(e))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n, x= map(int, input().split(' '))
    print(2**(x-n))
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n, x= map(int, input().split(' '))
    print(2**(x-n))
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        n,x=map(int,input().split())
        k=2**x
        for i in range(1,n+1):
                k=k-(0.5*k)
        print(int(k))
        