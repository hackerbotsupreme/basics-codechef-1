for _ in range(int(input())):
    a,b,c=[int(a) for a in input().split()]
    x=(400/a)
    y=(400/b)
    z=(400/c)
    
    if(max(x,y,z)==x):
        print("ALICE")
    elif(max(x,y,z)==z):
        print("CHARLIE")
    else:
        print("BOB")







# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    sa=400/a;
    sb=400/b;
    sc=400/c;
    if(sa>sb and sa>sc):
        print("ALICE")
    elif(sb>sa and sb>sc):
        print("BOB")
    else:
        print("CHARLIE")
        
        
        
from math import inf, lcm, gcd;
# ---------------------------------------- COLLECTIONS -----------------------------------------------#
from collections import defaultdict as maps #"""using this, we can give a default value of data type to dict"""
from collections import OrderedDict #"""this stores the order of insertion of values in dict"""
from collections import Counter as freq  #"""returns a dict containing count of values"""
from collections import ChainMap  #"""to have diff. dicts in one class (container)"""
#"""we have to use .new_child(new_dictToInsert) to insert a new dict into ChainMap"""
#---------------------------------------- COLLECTIONS ------------------------------------------------ #

def getlist():
    return list(map(int, input().split()))
    
def getinp():
    return map(int, input().split())
    
#----------------------------------------- MAIN CODE -------------------------------------------------#    
def main():
    for _ in range(int(input())):
        a,b,c = getinp()
        d = {a:'Alice',b:'Bob',c:'Charlie'}
        print(d[min(a,b,c)])
        
#----------------------------------------- MAIN CODE -------------------------------------------------#

if __name__ == "__main__":
    main()
    
    
    
# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a<b and a<c:
        print("Alice")
    elif b<a and b<c:
        print("Bob")
    else:
         print("Charlie")
         
         
         
# cook your dish here "divide distance by time"
for i in range(int(input())):
    x,y,z = map(int, input().split())
    Alice = 400/x 
    Bob = 400/y
    Charlie = 400/z
    
    if Alice > Bob and Alice > Charlie:
        print("Alice")
    elif Bob > Alice and Bob > Charlie:
        print("Bob")
    else:
        print("Charlie")
        
        
        
        
        
# cook your dish here "divide distance by time"
for i in range(int(input())):
    x,y,z = map(int, input().split())
    Alice = 400/x 
    Bob = 400/y
    Charlie = 400/z
    
    if Alice > Bob and Alice > Charlie:
        print("Alice")
    elif Bob > Alice and Bob > Charlie:
        print("Bob")
    else:
        print("Charlie")