for i in range(int(input())):
    a, c = map(int, input().split())
    b = int((a + c) / 2)
    if a == c:
        print(a)
    elif b - a == c - b:
        print(int(b))
    else:
        print(-1)
    





# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print((a+b)//2)
    else:
        print(-1)
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    a,c=map(int,input().split())
    b=(a+c)//2
    if c-b==b-a:
        print(b)
    else:
        print("-1")
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if(a+b)%2==0:
        print((a+b)//2)
    else:
        print(-1)
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    a,c=(map(int,input().split()))
    d=(a+c)//2
    e=a+c
    if e%2==0:
        print(d)
    else:
        print(-1)
