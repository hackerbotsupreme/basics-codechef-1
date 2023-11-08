# cook your dish here
import math
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    subscription = math.ceil(n/6)
    print(subscription*x)
    
    
    
    
    
    
# cook your dish here
import math
t=int(input())
for i in range(t):
        N,X=map(int,input().split())
        if N==1:
                print(X)
        else:
                print((math.ceil(N/6))*X)
                
                
                
                
# cook your dish here
for i in range(int(input())):
    n,x = map(int,input().split())
    if(n%6 == 0):print((n//6) * x)
    else:print((n//6+1)*x)
    
    
    
    
    
# cook your dish here
import math
for t in range(int(input())):
    n,x = map(int,input().split())
    print((math.ceil(n/6))*x)






