for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    alex = pow(x1, 2) + pow(y1, 2)
    bob = pow(x2, 2) + pow(y2, 2)
        
    if(alex > bob):
        print("Alex")
    elif(bob > alex):
        print("Bob")
    elif(alex == bob):
        print("Equal")
        
        
        
        
        
        
        
        
# cook your dish here
import math
for i in range(int(input())):
        a,b,c,d=map(int,input().split())
        if (math.sqrt(a*a+b*b)>math.sqrt(c*c+d*d)):
                print("Alex")
        elif (math.sqrt(a*a+b*b)<math.sqrt(c*c+d*d)):
                print("Bob")
        else:
                print("Equal")
                
                
                
                
                
                
                
                
# cook your dish here
import math
T = int(input())
for i in range (T):
    X1,Y1,X2,Y2 = map(int,input().split())
    Alice= math.sqrt(X1**2 + Y1**2)
    Bob = math.sqrt(X2**2 + Y2**2)
    
    if (Alice>Bob):
        print("Alex")
    elif (Bob>Alice):
        print("BOB")
    elif (Bob == Alice):
        print("Equal")
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
import math
t=int(input())
while t>0:
    x1,y1,x2,y2=map(int,input().split())
    a=math.sqrt((x1**2)+(y1**2))
    b=math.sqrt((x2**2)+(y2**2))
    if a>b:
        print("Alex")
    elif a<b:
        print("Bob")
    else:
        print("Equal")
    t=t-1
    
    
    
    
    
T = int(input())

for _ in range(T):
    (X1, Y1, X2, Y2) = map(int, input().split())
    Alex_distance = X1*X1 + Y1*Y1
    Bob_distance = X2*X2 + Y2*Y2
    if(Alex_distance == Bob_distance):
        print("EQUAL")
    elif Alex_distance > Bob_distance:
        print("ALEX")
    else:
        print("BOB")
        
        
        
        
        
        
        
        
        
        
        
        
