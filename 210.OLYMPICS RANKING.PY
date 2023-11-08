# cook your dish here
for _ in range(int(input())):
    s=list(map(int,input().split()))
    t1=sum(s[:3])
    t2=sum(s[3:])
    if t1>t2:
        print('1')
    else:
        print('2')
        
        
        
        
        
        
        
        
        
        
        
        
for t in range(int(input())):
    g1, s1, b1, g2, s2, b2 = map(int, input().split())
    if(g1 + s1 + b1 > g2 + s2 + b2):
        print("1")
    else:
        print("2")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
t=int(input())
for i in range(t):
    x,y,z,a,b,c=map(int,input().split())
    if x+y+z>a+b+c:
        print("1")
    else:
        print("2")
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        a,b,c,x,y,z=map(int,input().split())
        print(1) if max(a+b+c,x+y+z)==a+b+c else print(2)