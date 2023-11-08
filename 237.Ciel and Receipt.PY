# cook your dish here
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
t=int(input())
l=l[::-1]
for i in range(t):
    a=int(input())
    j=0
    ans=0
    while(a>0):
        if a<l[j]:
            j+=1
            continue
        else:
            a-=l[j]
            ans+=1
            j=0
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
for i in range(int(input())):
    p=int(input())
    m=0
    for j in range(12,0,-1):
        m=m+p//(2**(j-1))
        p%=2**(j-1)
    print(m)
    
    
    
    
    
    
    
# cook your dish here
t=int(input()) 
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
for _ in range(t):
    p=int(input())
    i=len(l)-1 
    c=0 
    while(i>=0 and p!=0):
        if l[i] > p:
            i-=1 
        else:
            p=p-l[i] 
            c+=1 
    print(c) 
    
    