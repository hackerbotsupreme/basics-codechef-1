# cook your dish here
t=int(input())
for i in range(t):
        a,b,c=map(int,input().split())
        print(max(a,b,c))
        
        
        
# cook your dish here
T=int(input())
for i in range(T):
    a=list(map(int,input().split()))
    print(max(a))
    
    
    
# cook your dish he
t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A>B:
        if A>C:
            print(A)
        else:
            print(C)
    else:
        if B>C:
            print(B)
        else:
            print(C)
            
            
            
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    l=[a,b,c]
    l.sort()
    print((l[2]))
    
    
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(max(a,b,c))