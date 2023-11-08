for _ in range(int(input())):
    a,b = map(int,input().split())
    if a > 0 and b > 0:
        print('Solution')
    elif b > 0:
        print('Liquid')
    else: print('Solid')
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if(a!=0 and b==0):
        print("Solid")
    elif(a==0 and b!=0):
        print("Liquid")
    else:
        print("Solution")
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    
  a,b=map(int,input().split())
  if a==0:
    print("Liquid")
  elif b==0:
    print("Solid")
  else:
    print("Solution")
    