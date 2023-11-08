# cook your dish here
for i in range(int(input())):
        x,y,z,m,a,b,c=map(int,input().split())
        print("YES") if (a>=x and b>=y and c>=z and a+b+c>=m) else print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if x==y:
        print(x+y-1)
    else:
        print(x+y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    uc=a-b
    if(uc==0):
        print(b*2+uc-1)
    else:
        print(b*2+uc)
        
        
        
        
        
        
        
        
        
        
        
for t in range(int(input())):
    x, y = map(int, input().split())
    if(x == y):
        print((y * 2) - 1)
    else:
        print(x + y)