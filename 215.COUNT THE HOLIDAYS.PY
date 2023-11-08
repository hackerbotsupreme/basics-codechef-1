# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        sat=[6,13,20,27]
        sun=[7,14,21,28]
        print(len(set(k+sat+sun)))
        
        
        
        
        
        
        
        
        
for i in range(int(input())):
    n=int(input())
    h1={6,7,13,14,20,21,27,28}
    h2=set(map(int,input().split()))
    h3=h1.union(h2)
    print(len(h3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
ss = [6,7,13,14,20,21,27,28]
for i in range(int(input())):
    n = int(input())
    f = list(map(int,input().split()))
    c = 0
    for j in f:
        if j not in ss:
            c+=1
    print(c+8)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    list1=[6,13,20,27,7,14,21,28]
    count=8;
    for i in a:
        if i not in list1:
                count+=1
    print(count)        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
h=[6,7,13,14,20,21,27,28]
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=8
    for i in l:
         if i not in h:
             c=c+1
    print(c)         