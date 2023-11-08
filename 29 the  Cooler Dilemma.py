# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=a*c
    if(d<b):
        print("YES")
    else:
        print("NO")
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(b>a*c):
        print("YES")
    else:
        print("NO")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
        X,Y,M=map(int,input().split())
        if(X*M<Y):
                print("YES")
        else:
                print("NO")
                
                
                
# cook your dish here
testcases = int (input ())
for i in range(testcases):
    rent, buy, months=map(int,input().split())
    if rent*months < buy:
        print ("YES")
    else:
        print("NO")
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    x,y,m = map(int,input().split())
    if(x*m <y):
        print("yes")
    else:
        print("no")