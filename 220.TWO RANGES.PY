# cook your dish here
t=int(input ())
for _ in range(t):
    a,b,c,d=map(int, input ().split())
    x=[]
    for i in range(a,b+1):
        x.append(i)
    for j in range(c,d+1):
        x.append(j)
    print (len(set(x)))
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    arr=[]
    for i in range(a,b+1):
        if(i not in arr):
            arr.append(i)
    for j in range(c,d+1):
        if(j not in arr):
            arr.append(j)
    print(len(arr))
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    m = {}
    for i in range(a,b+1):
        m[i] = i
    for i in range(c,d+1):
        m[i] = i
    print(len(m))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    x=[]
    for j in range(a,b+1):
        x.append(j)
    for k in range(c,d+1):
        x.append(k)
    print(len(set(x)))
        
        
        
        
        
        
        
        
        
        
        
