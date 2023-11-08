# cook your dish here
for i in range(int(input())):
    al=0
    n = int(input())
    women=list(map(int,input().split()))
    for j in women:
        if j>=10 and j<=60:
            al+=1
    print(al)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    el = 0
    for i in a:
        if i>=10 and i<= 60:
            el +=1
    print(el)        
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    k=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in a:
        if j>=10 and j<=60:
            k+=1
            
    print(k)