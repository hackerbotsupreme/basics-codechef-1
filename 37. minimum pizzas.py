# cook your dish here
T = int(input())
for tc in range(T):
	(n, x) = map(int, input().split(' '))
	
	pizza = n * x // 4
	
	if n*x % 4 == 0:
	    print(pizza)
	else:
	    print(pizza+1)
	
 
 
 
 
 
 
# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split()) 
    if (n*x) % 4 == 0:
        print(int((n*x)/4))
    else:
        print(int((n*x)/4)+1)
        
        
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    n,x=map(int,input().split())
    a=n*x%4
    if(a==0):
        print(n*x//4)
    else:
        print(n*x//4+1)
        
        
        
        
        
# cook your dish here
import math
for t in range(int(input())):
    n,x = map(int,input().split())
    s = math.ceil((n*x/4))
    print(s)
    
    
    
    
    
import math
T = int(input())
for i in range(T):
    (N, X) = map(int, input("").split(" "))
    ans = (N*X)/4
    print (math.ceil(ans))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
