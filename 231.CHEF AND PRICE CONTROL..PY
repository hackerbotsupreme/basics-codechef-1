for i in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))[:n]
    #print(p)
    l=[]
    for i in p:
        if(i>k):
            l.append(k)
        else:
            l.append(i)
    #print(l)
    print(sum(p)-sum(l))
    
    
    
    
    
    
    
    
    
# cook your dish here
# for _ in range(int(input())):
#     n,p=map(int,input().split())
#     arr=list(map(int,input().split()))
#     l=[]
#     c=0
#     for i in arr:
#         if(i>=p):
#             c+=1
#         else:
#             l.append(i)
#     if(c<n and c!=0):
#         print(sum(l)+(c*p))
#     elif(c==0):
#         print(0)
#     else:
#         print(n*p)
for i in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))[:n]
    #print(p)
    l=[]
    for i in p:
        if(i>k):
            l.append(k)
        else:
            l.append(i)
    print(sum(p)-sum(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        m=[]
        for i in l:
                if i>k:
                        m.append(k)
                else:
                        m.append(i)
        print(sum(l)-sum(m))
                        
                        
        