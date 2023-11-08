# cook your dish here

t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    if (x==a or x==b) and (y==b or y==a):
        print("0")
    elif (x==a or x==b) or (y==b or y==a):
        print("1")
    else:
        print("2")
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    if x in [a,b] and y in [a,b]:
        print(0)
    elif x in [a,b] or y in [a,b]:
        print(1)
    else:
        print(2)
        
        
        
        
        
t=int(input())
for i in range(0,t):
    x=set(map(int,input().split()))
    print(len(x)-2)
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        x,y,a,b=map(int,input().split())
        if len(set([x,y,a,b]))==len([x,y,a,b]):
                print(2)
        elif len(set([x,y,a,b]))==3:
                print(1)
        else:
                print(0)