# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    z=2*y
    print(x//z)
    
    
    
    
# cook your dish here
for i in range(int(input())):
        x,y=map(int,input().split())
        print(x//(2*y))
        
        
        
        
for _ in range(int(input())):
    x,y = map(int,input().split())
    print(x//(y*2))



from math import ceil, floor
for i in range(int(input())):
    x, y =map(int, input().split())
    one_person = y*2
    print(x//one_person)
    
    
# cook your dish here    
for i in range(int(input())):
    x,y=map(int,input().split())
    y=y*2
    if(x>=y):
        print(x//y)
    else:
        print("0")