# cook your dish here
for t in range(int(input())):
    a=list(map(int,input().split()))
    i=0
    j=0
    for k in range(len(a)):
        if(a[k]==1):
            i=i+1
        else:
            j=j+1
    if(i<j):
        print("NO")
    else:
        print("YES")
        
        
        
        
        
        
        
        
        
        
        
        
for _ in range(int(input())):
    A1,A2,A3,A4,A5,A6,A7 = map(int,input().split())
    if (A1 + A2 + A3 + A4 + A5 + A6 + A7) > 3:
        print('yes')
    else:
        print('no')
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  l = list(map(int,input().split()))
  p,q = 0,0
  for i in range(len(l)):
    if l[i]== 1:
      p = p + 1
    else:
      q = q + 1
  if p>q:
    print("YES")
  else:
    print("NO")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    c=0
    k=0
    a=list(map(int,input().split()))
    for j in a:
        if j==1:
            c+=1 
        else:
            k+=1 
            
    if c>k:
        print("yes")
    else:
        print("no")