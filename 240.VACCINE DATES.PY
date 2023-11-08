t = int(input())
for i in range(t):
    d,l,r = map(int,input().split())
    if(l<=d and r>=d):
        print("Take second dose now")
    elif(l>=d):
        print("Too Early")
    else:
        print("Too Late")
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for _ in range(t):
    d,l,r=map(int,input().split())
    if(d>=l and d<=r):
        print("Take second dose now")
    elif(d>r):
        print("Too Late")
    else:
        print("Too Early")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
def check(d,l,r):
    if d >= l and d <=r :
        return 'Take second dose now'
    elif d > l  and  d > r :
        return 'Too Late'
    else:
        return 'Too Early'


t=int(input())
for _ in range(t):
    d,l,r=map(int,input().split())
    print(check(d,l,r))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
for _ in range(int(input())):
    d,L,r = map(int,input().split())
    if d >= L and d <= r:
        print('Take second dose now')
    elif d > L:
        print('Too Late')
    else:
        print('Too Early')