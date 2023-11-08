t = int(input())
for i in range(t):
  a = list(map(int,input().split(' ')))
  count = 0
  count1 = 0
  for j in range(len(a)):
    if j%2 == 0:
      if a[j] == 1:
        count+=1
    else:
      if a[j] == 1:
        count1+=1
  if count > count1:
    print(1)    
  elif count == count1:
   print(0) 
  else:
   print(2)
   
   
   
   
   
   
   
   
   
   
   
   
   
# cook your dish here
for t in range(int(input())):
    A=0
    B=0
    index=0
    score=list(map(int,input().split()))
    for i in score:
        if index%2==0 and i==1:
            A+=1
        elif index%2!=0 and i==1:
            B+=1
        index+=1
    if A==B:
        print("0")
    elif A>B:
        print("1")
    elif B>A:
        print("2")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
t = int(input())
for i in range(t):
  a = list(map(int,input().split(' ')))
  count = 0
  count1 = 0
  for j in range(len(a)):
    if j%2 == 0:
      if a[j] == 1:
        count+=1
    else:
      if a[j] == 1:
        count1+=1
  if count > count1:
    print(1)    
  elif count == count1:
   print(0) 
  else:
   print(2)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
p=int(input())
for i in range(p):
    A,B,C,D,E,F,G,H,I,J=list(map(int,input().split()))
    r=A+C+E+G+I
    t=B+D+F+H+J
    if r>t:
        print(1)
    elif t>r:
        print(2)
    else:
        print(0)