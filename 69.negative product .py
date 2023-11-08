for t in range(int(input())):
    a, b, c = map(int, input().split())
    if(a * b < 0 or b * c < 0 or c * a < 0):
        print("Yes")
    else:
        print("No")
        
        

# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(a*b<0 or b*c<0 or c*a<0):
        print("YES")
    else:
        print("NO")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(a*b<0 or b*c<0 or a*c<0):
        print("YES") 
    else:
        print("NO")
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    a,b,c=map(int,input().split())
    if(c*a >=0  and c*b>=0 and a*b>=0):
        print('no')
    else:
        print('yes')