t = int(input())
for i in range(t):
    h,x,y,c = map(int,input().split(' '))
    g=x+int(y/2)
    m=g*h
    if m <= c:
      print("yes")
    else:
      print("no")  
      
      
      
      
      
      
      
      
      
      
      
      
for tc in range(int(input())):
    h,x,y,c=map(int,input().split())
    greywater=x + y//2
    consumption = h*greywater
    if(consumption<=c):
        print("yes")
    else:
        print("no")
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
        h,x,y,c=map(int,input().split())
        print("YES") if (x+y//2)*h<=c else print("NO")