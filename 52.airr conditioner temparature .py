# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    x=min(a,b,c)
    y=max(a,b,c)
    flag=False
    for i in range(x,y+1):
        if i>=a and i<=b and i>=c:
            flag=True
            break
    if flag==True:
        print("YES")
    else:
        print("NO")
        
        
        
        
# cook your dish here
t=int(input())
for t in range(t):
    a,b,c=map(int,input().split())
    if(a<=b and c<=b):
        print("yes")
    else:
        print("no")
        
        
        
        
for _ in range(int(input())):
    x,y,z=map(int,input().split(" "))
    if y>=x and y>=z:
        print("Yes")
    else:
        print("No")
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    x=min(a,b,c)
    y=max(a,b,c)
    flag=False
    for i in range(x,y+1):
        if i>=a and i<=b and i>=c:
            flag=True
            break
    if flag:
        print("YES")
    else:
        print("NO")