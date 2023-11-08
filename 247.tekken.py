# cook your dish here
t=int(input())
for i in range (t):
    x,y,z=map(int,input().split())
    p=x
    q=y
    r=z
    a=min(x,y)
    x=x-a
    y=y-a
    b=min(y,z)
    y=y-b
    z=z-b
    c=min(x,z)
    x=x-c
    z=z-c
    if x>0:
        print("YES")
    else:
       a=min(q,r)
       q=q-a
       r=r-a
       b=min(p,q)
       p=p-b
       q=q-b
       c=min(p,r)
       p=p-c
       r=r-c
       if p>0:
           print("YES")
       else:
           print("NO")
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    min3=min(b,c)
    p=b-min3
    q=c-min3
    sum=p+q
    if a!=0 and a>sum:
        print("Yes")
    else:
        print("No")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t = int(input())
for i in range(0,t):
    a,b,c = map(int,input().split())
    x = min(b,c)
    b = b - x
    c = c - x
    if(a > max(b,c)):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a-(abs(b-c))>0):
        print("YES")
    else:
        print("NO")