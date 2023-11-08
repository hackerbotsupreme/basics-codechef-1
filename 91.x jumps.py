goals = int(input())
for distractions in range(goals):
    life, wife = map(int, input().split())
    print((life % wife) + (life // wife))
    
    
    
    
    
    
    
    
# cook your dish here
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    print(x%y+x//y)
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    X,Y= map(int,input().split())
    print(X%Y + X//Y)
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    print(x%y+x//y)
    
    
    







for _ in range(int(input())):
    x,y=map(int,input().split(" "))
    if x>=y:
        if x%y==0:
            print(int(x/y))
        else:
            a=int(x/y)
            b=(x-(a*y))
            print(a+b)
    else:
        print(x)
            
        
        
        
    