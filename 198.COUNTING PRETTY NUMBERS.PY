t = int(input())
if(t >= 1 and t <= 100):
    for _ in range(t):
        l, r = map(int, input().split())
        c = 0
        if l >= 1 and l <= r and r <= (pow(10, 5)):
            for i in range(l, r+1, 1):
                if i%10==2 or i%10==3 or i%10==9:
                    c+=1
            print(c)
            
            
            
            
            
            
            
            
# cook your dish here
for i in range(int(input())):
  L,R = map(int,input().split())
  count = 0
  l = [2,3,9]
  for i in range(L,R+1):
    if i%10 in l:
      count+=1
  print(count)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# cook your dish here
for i in range(int(input())):
    c=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        if i%10==2 or i%10==3 or i%10==9:
            c+=1
    print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        l,r=map(int,input().split())
        c=0
        if l >= 1 and l <= r and r <= (pow(10, 5)):
            for i in range(l, r+1, 1):
                if i%10==2 or i%10==3 or i%10==9:
                    c+=1
            print(c)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        l,r=map(int,input().split())
        c=0
        if l >= 1 and l <= r and r <= (pow(10, 5)):
            for i in range(l, r+1, 1):
                if i%10==2 or i%10==3 or i%10==9:
                    c+=1
            print(c)
        