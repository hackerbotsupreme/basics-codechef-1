n = int(input())
for _ in range(n):
    r1,r2,r3 = map(int,input().split())
    if r1 > (r2+ r3 )or r2 > (r3+ r1) or r3 > (r1 + r2):
        print('yes')
    else:
        print('no')
        
        
        
n = int(input())
for _ in range(n):
    r1,r2,r3 = map(int,input().split())
    if r1 > r2+ r3 or r2 > r3+ r1 or r3 > r1 + r2:
        print('yes')
    else:
        print('no')
        




for i in range(int(input())):
    l = list(map(int,input().split()))
    if max(l) > (sum(l) - max(l)):
        print("YES")
    else:
        print("nO")
        
        
        



for i in range(int(input())):
    a,b,c = map(int, input().split())
    if (a + b) < c or (b + c) < a or (a + c) < b:
        print('Yes')
    else:
        print('No')
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a+b<c or b+c<a or a+c<b):
        print("Yes")
    else:
        print("No")
        
        
        
        
        
n = int(input())
for _ in range(n):
    r1,r2,r3 = map(int,input().split())
    if r1 > r2+ r3 or r2 > r3+ r1 or r3 > r1 + r2:
        print('yes')
    else:
        print('no')
        
        