# cook your dish here
for _ in range(int(input())):
    ball,box=map(int,input().split())

    if ball<=box and (ball!=1 and box!=1) :
        print('NO')
    else:
        if ball>=((box*(box+1))/2):
            print('YES')
        else:
            print("NO")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    req = k*(k+1)//2
    if n>=req:
        print('YES')
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    p=(k*(k+1))/2
    if n<=k and n!=1 and k!=1:
        print('no')
    elif n>=p:
        print('yes')
    else:
        print('no')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
for _ in range(int(input())):
    n,k=map(int,input().split())
    print("NO") if n<(k*(k+1))/2 else print("YES")