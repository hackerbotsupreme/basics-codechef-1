# cook your dish here
def check(num):
    if num[::-1] == num:
        return True
    return False

for T in range(int(input())):
    N = input()
    print("wins" if check(N) else "loses")
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        n=(input())
        print("wins") if n==n[::-1] else print("loses")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    n=int(input())
    b=0
    c=n
    while(c):
        a=c%10
        b=b*10+a
        c=c//10
    if(b==n):
        print("wins")
    else:
        print("loses")
        
        
        
        
        
        
        
        
        
        
        
# The Block Game
for i in range(int(input())):
    m=0
    n=input()
    k=''
    for j in n:
        k=j+k
    if(n==k):
        print("wins")
    else:
        print("loses")
        