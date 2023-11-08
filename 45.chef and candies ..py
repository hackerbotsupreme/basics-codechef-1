for i in range(int(input())):
    n,x=map(int,input().split())
    if(n>=x):
        n=n-x 
        if(n%4==0):
            print(n//4)
        else:
            print((n//4)+1)
    else:
        print(0)
        
        
        
        


t=lambda x,y:0if x<y else(x-y)//4+int((x-y)%4!=0)
for _ in[I:=input]*int(I()):x,y=map(int,I().split());print(t(x,y))







# cook your dish here
import math
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=n-x
    if(x>=n):
        print("0")
    else:
        print(math.ceil(a/4))
        
        
        
        
# cook your dish here
for i in range(int(input())):
    children, candy = map(int, input().split(" "))
    remaining = children - candy
    if(remaining>0):
        if(remaining%4 == 0):
            print(remaining//4)
        else:
            print(remaining//4 +1)
    else:
        print(0)
        
        
        
        
# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    if n<x:
        print("0")
        continue
    n=n-x
    if n%4==0:
        print(n//4)
    else:
        print((n//4)+1)
    