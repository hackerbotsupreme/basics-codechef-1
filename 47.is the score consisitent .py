# cook your dish here
for i in range(int(input())):
    a,b = map(int, input().split(" "))
    c,d = map(int, input().split(" "))
    if(c>=a and d>=b):
        print("Possible")
    else:
        print("Impossible")
        
        
# cook your dish here
t=int(input())
for t in range(t):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if(a<=c and b<=d):
        print('possible')
    else:
        print('impossible')
        
        
        
        
for i in range(int(input())):
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    
    if a > c or b > d:
        print('impossible')
    else:
        print('possible')
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if(a<=c and b<=d):
        print("possible")
    else:
        print("impossible")
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if a<=c and b<=d:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')