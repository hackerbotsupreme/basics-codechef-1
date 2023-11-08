for _ in range(int(input())):
    c=0
    l,m=[],[]
    k=int(input())
    s=input()
    for i in range(0,k//2):
        l.append(s[i])
    for i in range((k//2),k):
        m.append(s[i])
    if l==m:
        print("YES")
    else:
        print("NO")
            
            
            
            
            
            
            
            
            
            
            
for _ in range(int(input())):
    c=0
    l,m=[],[]
    k=int(input())
    s=input()
    for i in range(0,k//2):
        l.append(s[i])
    for i in range((k//2),k):
        m.append(s[i])
    if l==m:
        print("YES")
    else:
        print("NO")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# cook your dish here
for i in range(int(input())):
    l,m=[],[]
    n=int(input())
    s=input()
    for k in range(0,n//2):
        l.append(s[k])
    for j in range(n//2,n):
        m.append(s[j])
    if(l==m):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
# cook your dish here
n=int(input())
for i in range(1,n+1):
    x=int(input())
    a=input()
    l=len(a)
    m=""
    
    h=""
    for z in range(0,int(l/2)):
        d=a[z]
        m=m+d
    for y in range(int(l/2),int(l)):
        j=a[y]
        h=h+j 
    s=h+m 
    if(s==a):
        print("YES")
    else:
        print("NO")
            
