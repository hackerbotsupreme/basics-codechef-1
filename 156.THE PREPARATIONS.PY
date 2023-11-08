# cook your dish here


def solve():

    x, y, z = map(int, input().split())
    
    if y*z < x:
        return "YES"
    else:
        return 'NO'

n = int(input())

for _ in range(n):
    print(solve())
    
















# cook your dish here
for i in range(int(input())):
        m,n,k=map(int,input().split())
        print("YES") if n*k<m else print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
for _ in range(int(input())):
    m,n,k = map(int,input().split())
    if (n*k) < m:
        print('yes')
    else:
        print('no')
















# cook your dish here
t = int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    if(m>n*k):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    s=n*k 
    if m>s:
        print("yes")
    else:
        print("no")