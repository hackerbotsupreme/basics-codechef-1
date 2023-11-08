# cook your dish here
n=int(input())
for i in range(n):
    c=list(map(int,input().split()))
    if c[0]>c[1]:
        print("CAR")
    elif c[1]>c[0]:
        print("BIKE")
    else:
        print("SAME")
        
        
        
        
for _ in range(int(input())):
    x,y = map(int,input().split())
    if x < y:
        print('BIKE')
    elif x > y:
        print('CAR')
    else:
        print('SAME')
    
    
    
# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print("SAME")
    elif x==min(x,y):
        print("BIKE")
    else:
        print("CAR")


# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print("SAME")
    elif x==min(x,y):
        print("BIKE")
    else:
        print("CAR")




for _ in range(int(input())):
    x,y=map(int,input().split(" "))
    if x<y:
        print("BIKE")
    elif y<x:
        print("CAR")
    else:
        print("SAME")