# cook your dish here
T = int(input())
for tc in range(T):
    # x=Chef , Y=Chefina, K=Move per step
    (x, y, k) = map(int, input().split(' '))
    
    diff = abs(y - x)
    move = diff // k 
    if diff%k > 0:
        move += 1 
    print(move)
    
    
    
    
    
    
# cook your dish here
import math
for i in range(int(input())):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))
    
    
    
    
    
    
    
    
# cook your dish here
import math
for i in range(int(input())):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
import math
t = int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))
    
    
    
    
    
    
    
    
    
# cook your dish here
import math
t = int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    print(math.ceil(abs(x-y)/k))