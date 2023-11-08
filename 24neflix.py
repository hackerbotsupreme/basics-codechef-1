for _ in range(int(input())):
    a,b,c,x=map(int,input().split())
    if(a+b>=x or b+c>=x or a+c>=x):
        print("YES")
    else:
        print("NO")
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if((a+b)>=d or (a+c)>=d or (b+c)>=d):
        print("YES")
    else:
        print("NO")
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
  A,B,C,X = map(int,input().split())
  if (A+B)>=X or (B+C)>=X or (C+A)>=X:
    print("YES")
  else:
    print("NO")
    
    
    
    
# cook your dish here
t = int(input())
for i in range(t):
    a,b,c,x = map(int,input().split())
    if(a+b>=x or b+c>=x or a+c>=x):
        print("YES")
    else:
        print("NO")
    
    
    
    
for _ in range(int(input())):
    arr = list(map(int,input().split(" ")))
    #seperating cost from array
    cost=arr[3]
    arr.pop()
    #sorting array and taking 2 highest values
    arr.sort()
    add=arr[1]+arr[2]
    
    #if the sum of 2 highest values can afford the subscription then certainly YES
    if add>=cost:
        print("YES")
    else:
        print("NO")