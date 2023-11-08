# cook your dish here
t=int(input())
for i in range(t):
    def factrorial(n):
        if n==0:
            return 1
        else:
            result= n*factrorial(n-1)
            return result
    l=int(input())
    print(factrorial(l))
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n = int(input())
    x=1
    for i in range(1,n+1):
        x=x*i
    print(x)
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
import math
for i in range(int(input())):
        print(math.factorial(int(input())))
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    n=int(input())
    p=1
    for i in range(1,n+1):
        p=p*i
    print(p)









# cook your dish here
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

for _ in range(int(input())):
    n=int(input())
    print(factorial(n))