# cook your dish here
for i in range(int(input())):
        x,y,z=map(int,input().split())
        if min(x,y,z)==z:
                print("Alice")
        elif min(x,y,z)==y:
                print("Bob")
        else:
                print("Draw")
                
                
                
                
                
                
                
                
t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if(a<b and a<c):
        print("Draw")
    elif(b<c):
        print("Bob")
    else:
        print("Alice")
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for z in range(int(input())):
    a,b,c=map(int,input().split())
    if(c<a and c<b):
        print("Alice")
    elif(b<a and b<c):
        print("Bob")
    else:
        print("Draw")
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    sa,sb,sc=map(int,input().split())
    if sa < sb and sa <sc:
        print("draw")
    elif sb<sa and sb <sc:
        print("Bob")
    else:
        print("Alice")